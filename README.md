# FastAPI Celery Redis Blueprint Project

## Installation

### Redis

#### Using Docker

1. Install Docker: Follow the installation instructions for your operating system on the official Docker website: https://docs.docker.com/get-docker/

2. Run the Redis container:  
   `docker run -d -p 6379:6379 --name my-redis redis`
#### Using Local 
1. Install Redis:
    ```
   sudo apt-get update
   sudo apt-get install redis-server
   sudo systemctl start redis
   ```
2. Check if Redis is running: `redis-cli ping`
3. If you get a response of `PONG`, then Redis is running.

### Flower

1. Install Flower:  
`pip install flower`

### Nginx and SSL

1. Install Nginx:
```
sudo apt update  
sudo apt upgrade  
sudo apt install nginx
```

2. Install certbot:
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d your_domain_or_ip
```

3. Configure Nginx:  
`sudo nano /etc/nginx/sites-available/default`  
```
server {
    listen 443 ssl default_server;
    listen [::]:443 ssl default_server;
    server_name your_domain_or_ip;
    ssl_certificate /etc/letsencrypt/live/your_domain_or_ip/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your_domain_or_ip/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;

    location / {
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
`sudo systemctl restart nginx
`  

4. firewall:  
`sudo ufw allow https`     

5. Create worker systemd service:  
```
[Unit]
Description=Gunicorn instance to serve FastAPI app
After=network.target

[Service]
User=your_user
Group=your_group
WorkingDirectory=/path/to/your/fastapi/project
Environment="PATH=/path/to/your/fastapi/project/venv/bin"
ExecStart=/path/to/your/fastapi/project/venv/bin/gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 main:app

[Install]
WantedBy=multi-user.target

```
`sudo nano /etc/systemd/system/celery@.service
   `
```
[Unit]
Description=Celery Worker %I
After=network.target

[Service]
Type=simple
User=your_user
Group=your_group
WorkingDirectory=/var/www/service
Environment="PATH=/var/www/service/venv/bin"
ExecStart=/var/www/service/venv/bin/celery -A app.celery worker --concurrency=1 --loglevel=info --hostname=worker-%i@%%h -Q queue-%i,sum_queue,divide_queue -E
Restart=always
RestartSec=10s

[Install]
WantedBy=multi-user.target
```  
```
sudo systemctl daemon-reload

sudo systemctl start celery@1
sudo systemctl enable celery@1

sudo systemctl start celery@2
sudo systemctl enable celery@2

sudo systemctl start celery@3
sudo systemctl enable celery@3

sudo systemctl status celery@1

```  
6. Create flower systemd service:  
`sudo nano /etc/systemd/system/flower.service
   `
```
[Unit]
Description=Flower Celery Monitoring Tool
After=network.target

[Service]
Type=simple
User=your_user
Group=your_group
WorkingDirectory=/var/www/service
Environment="PATH=/var/www/service/venv/bin"
ExecStart=/var/www/service/venv/bin/celery -A app.celery flower --broker=redis://127.0.0.1:6379/0 --port=5555
Restart=always
RestartSec=10s

[Install]
WantedBy=multi-user.target
```  
```
sudo systemctl daemon-reload
sudo systemctl start flower.service
sudo systemctl enable flower.service
sudo systemctl status flower.service
```

## Commands:  
* launch flower dashboard: `celery -A main.celery flower --address=0.0.0.0 --port=5555 -l INFO`  or use one of the tasks: 
`celery -A app.tasks.divide_task flower --address=0.0.0.0 --port=5555 -l INFO` or `celery -A app.celery flower` for the general worker
* launch celery task1 worker: `celery -A app.tasks.divide_task worker -l info -n divide_worker@%h -Q divide_queue -E` 
* launch celery task2 worker: `celery -A app.tasks.sum_task worker -l info -n sum_worker@%h -Q sum_queue -E`
* launch celery worker for both tasks: `celery -A app.tasks.divide_task worker -l info -E -n worker1 -Q sum_queue,divide_queue`
* launch general worker: `celery -A app.celery worker --concurrency=1 --loglevel=info -Q sum_queue,divide_queue -E`
* Launch celery events: `celery -A app.tasks.divide_task events`  use any of the two tasks. This command starts the events viewer and monitors events related to both the sum_task and divide_task. As tasks are received, started, and completed, the events viewer will display information about them.

Other links:
* Documentation about monitoring: https://docs.celeryq.dev/en/stable/userguide/monitoring.html