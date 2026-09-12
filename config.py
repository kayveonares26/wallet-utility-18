import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth.llamarpc.com",
    "timeout": 30,
    "max_retries": 3,
    "enable_logging": True,
    "gas_multiplier": 1.1
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration from a JSON file, merging with defaults."""
        config = DEFAULT_CONFIG.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        config.update(file_config)
            except (json.JSONDecodeError, OSError):
                # Fallback to defaults on error
                pass
        return config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key with optional fallback."""
        return self.config.get(key, default)
