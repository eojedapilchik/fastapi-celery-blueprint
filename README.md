# adedayo-lotto-service

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



## Commands:  
* launch flower dashboard: `celery -A main.celery flower --address=0.0.0.0 --port=5555 -l INFO`  or use one of the tasks: 
`celery -A app.tasks.divide_task flower --address=0.0.0.0 --port=5555 -l INFO`
* launch celery task1 worker: `celery -A app.tasks.divide_task worker -l info -n divide_worker@%h -Q divide_queue -E` 
* launch celery task2 worker: `celery -A app.tasks.sum_task worker -l info -n sum_worker@%h -Q sum_queue -E`
* launch celery worker for both tasks: `celery -A app.tasks.divide_task worker -l info -E -n worker1 -Q sum_queue,divide_queue`
* launch general worker: `celery -A app.celery worker --concurrency=1 --loglevel=info -Q sum_queue,divide_queue -E`
* Launch celery events: `celery -A app.tasks.divide_task events`  use any of the two tasks. This command starts the events viewer and monitors events related to both the sum_task and divide_task. As tasks are received, started, and completed, the events viewer will display information about them.

Other links:
* Documentation about monitoring: https://docs.celeryq.dev/en/stable/userguide/monitoring.html