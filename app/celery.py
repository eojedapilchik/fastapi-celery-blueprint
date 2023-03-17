# this is a general worker
from celery import Celery
# Import the tasks explicitly
from .tasks import divide_task, sum_task
celery = Celery("app")

# Load the configuration from the 'celeryconfig.py' file
celery.config_from_object("app.celeryconfig")

# Register the tasks explicitly
celery.tasks.register(divide_task.divide_task)
celery.tasks.register(sum_task.sum_task)