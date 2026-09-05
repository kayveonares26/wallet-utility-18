import os
import logging
from typing import Optional

class ConfigError(Exception):
    """Custom exception for configuration failures."""
    pass

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves env var with validation for crypto keys."""
    value = os.getenv(key, default)
    if value is None:
        raise ConfigError(f"Missing required environment variable: {key}")
    
    # Security validation for hex strings
    if "KEY" in key and len(value) < 32:
        raise ConfigError(f"Invalid length for sensitive key: {key}")
    
    return value

try:
    RPC_URL = get_env_variable("RPC_URL")
    PRIVATE_KEY = get_env_variable("PRIVATE_KEY")
    CHAIN_ID = int(get_env_variable("CHAIN_ID", "1"))
except (ConfigError, ValueError) as e:
    logging.error(f"Critical configuration failure: {e}")
    raise SystemExit("Application halted due to invalid configuration") from e