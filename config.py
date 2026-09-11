import os
import logging
from typing import Any

class ConfigError(Exception):
    """Custom exception for configuration failures."""
    pass

def get_env_var(key: str, default: Any = None, required: bool = False) -> Any:
    """Retrieves environment variables with validation logic."""
    value = os.getenv(key, default)
    
    if required and value is None:
        raise ConfigError(f"Missing mandatory environment variable: {key}")
        
    return value

def load_network_config() -> dict:
    """Loads and validates crypto network parameters."""
    try:
        rpc_url = get_env_var("RPC_ENDPOINT", required=True)
        chain_id = int(get_env_var("CHAIN_ID", 1))
        timeout = float(get_env_var("REQUEST_TIMEOUT", 30.0))
        
        return {
            "rpc_url": rpc_url,
            "chain_id": chain_id,
            "timeout": timeout
        }
    except (ValueError, TypeError) as e:
        logging.error(f"Invalid configuration format: {e}")
        raise ConfigError("Failed to parse network settings") from e
    except ConfigError as e:
        logging.error(f"Required config missing: {e}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error during config load: {e}")
        raise ConfigError("Initialization failure") from e