import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {config_path}: {e}")
            
    return config

def get_network_config(config: Dict[str, Any]) -> str:
    """Extract network setting from config dict."""
    return str(config.get("network", "mainnet"))

if __name__ == "__main__":
    # Example usage for wallet-utility-18
    active_config = load_config()
    print(f"Loaded config: {active_config}")