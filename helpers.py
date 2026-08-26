import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Callable:
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        logger.error(f"Failed {func.__name__} after {max_retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def sanitize_address(address: str) -> str:
    """Validate and clean crypto wallet address strings."""
    if not isinstance(address, str):
        raise ValueError("Address must be a string")
    cleaned = address.strip()
    if not cleaned:
        raise ValueError("Address cannot be empty")
    return cleaned