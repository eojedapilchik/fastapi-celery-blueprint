# logging_config.py
import logging
import logging.handlers
from dotenv import load_dotenv
import os

load_dotenv()  # load the environment variables from .env file

loggers = {}


def get_logger():
    # if loggers.get("webservice"):
        # return loggers.get("webservice")
    log_file = os.getenv("LOG_FILE_LOCATION")
    logger = logging.getLogger('webservice')
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
    handler.setFormatter(formatter)
    logger.propagate = False
    logger.addHandler(handler)
    # logging.getLogger("webservice").propagate = False
    # loggers["webservice"] = logger
    return logger
