import os
import logging
import logging.config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'logger_config.ini')

def log_event(username: str, status: str):
    logging.config.fileConfig(CONFIG_PATH, disable_existing_loggers=False)
    logger = logging.getLogger()

    if status == 'success':
        logger.info(f"User '{username}' logged in successfully.")
    elif status == 'expired':
        logger.warning(f"User '{username}' attempted login with expired credentials.")
    elif status == 'failed':
        logger.error(f"User '{username}' failed to login.")
    else:
        logger.error(f"User '{username}' encountered an unknown login status: {status}.")
