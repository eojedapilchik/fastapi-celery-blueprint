# app/tasks/divide_task.py
import time
from celery import Celery
from logging_config import get_logger

celery_app = Celery("divide_task")
celery_app.config_from_object("app.celeryconfig")
logger = get_logger()


@celery_app.task
def divide_task(a: float, b: float):
    logger.info("Processing tasks divide_task...")
    time.sleep(20)
    result = a / b
    logger.info(f"Result of dividing {a} by {b}: {result}")
    return result
