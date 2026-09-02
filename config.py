import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Default settings for logger in wallet-utility-18
DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "wallet_utility.log"
DEFAULT_MAX_BYTES = 10 * 1024 * 1024  # 10 MB
DEFAULT_BACKUP_COUNT = 5
DEFAULT_LOG_LEVEL = logging.INFO

def setup_logger(
    name: str = "wallet_utility",
    log_dir: str = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    level: int = DEFAULT_LOG_LEVEL,
    max_bytes: int = DEFAULT_MAX_BYTES,
    backup_count: int = DEFAULT_BACKUP_COUNT
) -> logging.Logger:
    """Configure a logger with rotating file handler and console output.
    Creates log directory if it does not exist.
    """
    # Ensure log directory exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    full_log_path = log_path / log_file
    # Get or create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Avoid adding duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()
    # Formatter for logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # Rotating file handler
    file_handler = RotatingFileHandler(
        full_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setLevel(logging.DEBUG)  # Log more to file
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("Logger initialized with rotation")
    return logger

# Module level logger instance for easy import
logger = setup_logger()