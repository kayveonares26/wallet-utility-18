import json
import os
from typing import Dict, Any, Optional

# Default configuration values for wallet-utility-18
DEFAULTS = {
    "network": "mainnet",
    "rpc_url": "https://mainnet.example.com",
    "api_key": None,
    "timeout": 30,
    "max_retries": 3,
    "log_level": "INFO",
    "wallet_dir": "./wallets",
    "confirmations_required": 1,
}

def load_configuration(config_file: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration with defaults, overriding from file and environment."""
    config = DEFAULTS.copy()

    # Load from file if provided and exists
    if config_file and os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                file_config = json.load(f)
                if isinstance(file_config, dict):
                    config.update(file_config)
        except (json.JSONDecodeError, IOError) as e:
            # In production would log, but for now ignore or print
            print(f"Warning: Could not load config file: {e}")

    # Override with environment variables
    for key in list(config.keys()):
        env_key = f"WALLET_{key.upper()}"
        if env_key in os.environ:
            value = os.environ[env_key]
            # Try to convert to original type if possible
            original = config[key]
            if isinstance(original, int):
                try:
                    config[key] = int(value)
                except ValueError:
                    pass
            elif isinstance(original, bool):
                config[key] = value.lower() in ("true", "1", "yes")
            else:
                config[key] = value

    return config

# Example usage
if __name__ == "__main__":
    cfg = load_configuration("wallet_config.json")
    print("Loaded config:", cfg)