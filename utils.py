import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger("wallet-utility-18")

def retry_operation(
    max_attempts: int = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Decorator implementing exponential backoff for network operations."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay_seconds
            attempt = 1
            
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts. Error: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} for {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
                    attempt += 1
                    
        return wrapper
    return decorator
