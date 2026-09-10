import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network-dependent functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Max retries reached. Final error: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3, delay=2.0)
def fetch_balance(address: str):
    """Example of a network call for crypto balance."""
    # Placeholder for actual network request logic
    return 0.0