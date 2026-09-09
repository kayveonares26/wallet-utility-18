import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = 'wallet_utility', log_file: str = 'logs/wallet.log') -> logging.Logger:
    """
    Configures and returns a logger with console and rotating file handlers
    tailored for crypto wallet transaction auditing.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if re-imported or re-called
    if logger.handlers:
        return logger

    # Standardized format incorporating timestamp and log level
    log_format = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler for real-time monitoring
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # Rotating File Handler to persist transaction and network history
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10 MB rotation limit
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    except OSError as e:
        logger.warning(f'Could not establish file log handler: {e}. Defaulting to console only.')

    return logger

# Instantiate the default utility logger for global use
logger = setup_logger()
