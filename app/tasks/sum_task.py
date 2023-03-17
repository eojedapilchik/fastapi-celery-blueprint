# app/tasks/sum_task.py
import time
from celery import Celery

celery_app = Celery("sum_task")
celery_app.config_from_object("app.celeryconfig")


@celery_app.task
def sum_task(a: float, b: float):
    result = a + b
    print("Processing tasks sum_task...")
    time.sleep(20)
    print(f"Result of summing {a} and {b}: {result}")
    return result
