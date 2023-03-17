# app/tasks/divide_task.py
import time
from app.celery import celery_app
from logging_config import get_logger

logger = get_logger()


@celery_app.task(bind=True, max_retries=3)
def divide_task(self, a: float, b: float):
    logger.info("Processing tasks divide_task...")
    print("Processing tasks divide_task...")
    time.sleep(20)
    try:
        result = a / b
        logger.info(f"Result of dividing {a} by {b}: {result}")
    except ZeroDivisionError as e:
        # If the error is recoverable, retry the task
        raise self.retry(exc=e)
    return result
