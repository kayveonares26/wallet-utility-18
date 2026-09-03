import time
import random
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(func: Callable, max_attempts: int = 3, base_delay: float = 1.0) -> Any:
    """Executes a network-dependent function with exponential backoff."""
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Unrecoverable error: {e}")
            raise
            
    logger.error(f"Max retries reached. Final error: {last_exception}")
    raise last_exception

# Usage example for blockchain RPC calls
def fetch_balance(address: str):
    def task():
        # Simulated network call
        return "10.5 ETH"
    
    return with_retry(task, max_attempts=3)