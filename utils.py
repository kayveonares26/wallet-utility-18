import time
import logging
from functools import wraps
from requests.exceptions import RequestException

logger = logging.getLogger('wallet-utility-18')

def retry_network_operation(max_attempts=3, delay=2, backoff=2):
    """
    Decorator to retry network operations with exponential backoff.
    Specific to handling unstable crypto RPC node connections.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except RequestException as e:
                    if attempt == max_attempts:
                        logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts. Error: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} for {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator
