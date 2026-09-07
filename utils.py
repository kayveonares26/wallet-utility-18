import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(retries: int = 3, backoff: float = 1.0):
    """Decorator for retrying unstable network requests."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    wait = backoff * (2 ** attempt)
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
            logger.error(f"Final attempt failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator