# this is a general worker
from celery import Celery
# Import the tasks explicitly

celery_app = Celery("app")

# Load the configuration from the 'celeryconfig.py' file
celery_app.config_from_object("app.celeryconfig")
celery_app.autodiscover_tasks(["app.tasks"])
