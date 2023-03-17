# app/tasks/divide_task.py
import time
from app.celery import celery_app
from logging_config import get_logger

logger = get_logger()


@celery_app.task
def divide_task(a: float, b: float):
    logger.info("Processing tasks divide_task...")
    print("Processing tasks divide_task...")
    time.sleep(20)
    result = a / b
    logger.info(f"Result of dividing {a} by {b}: {result}")
    return result
