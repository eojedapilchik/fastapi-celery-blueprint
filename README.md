# adedayo-lotto-service


commands:  
* launch flower dashboard: `celery -A main.celery flower --address=0.0.0.0 --port=5555 -l INFO`    
* launch celery worker: `celery -A main.celery worker --loglevel=info` 
* Launch celery events: `celery -A main.celery events`

Other links:
* Documentation about monitoring: https://docs.celeryq.dev/en/stable/userguide/monitoring.html