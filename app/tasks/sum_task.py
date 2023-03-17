# app/tasks/sum_task.py
import time
from app.celery import celery_app
from logging_config import get_logger

logger = get_logger()


@celery_app.task
def sum_task(a: float, b: float):
    result = a + b
    logger.info("Processing tasks sum...")
    time.sleep(20)
    logger.info(f"Result of summing {a} and {b}: {result}")
    return result
