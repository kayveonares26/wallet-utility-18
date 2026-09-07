import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("wallet_utility.utils")

def retry_on_failure(
    retries: int = 3,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a function call with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {delay:.1f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator