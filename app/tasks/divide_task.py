# app/tasks/divide_task.py
import time
from celery import Celery

celery_app = Celery("divide_task")
celery_app.config_from_object("app.celeryconfig")


@celery_app.task
def divide_task(a: float, b: float):
    print("Processing tasks divide_task...")
    time.sleep(20)
    result = a / b
    print(f"Result of dividing {a} by {b}: {result}")
    return result
