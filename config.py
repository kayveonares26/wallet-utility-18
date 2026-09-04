import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "rpc_url": "https://mainnet.infura.io/v3/"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}")

    return config

def get_rpc_url(config: Dict[str, Any]) -> str:
    """Returns RPC URL from config or environment variable."""
    return os.getenv("RPC_URL", config.get("rpc_url", DEFAULT_CONFIG["rpc_url"]))

if __name__ == "__main__":
    # Verification of default loader logic
    active_config = load_config()
    print(f"Loaded network: {active_config['network']}")