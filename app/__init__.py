# Import the Celery app
from .celery import celery_app

# Import the tasks
from .tasks import divide_task, sum_task