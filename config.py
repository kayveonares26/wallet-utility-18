import os
import json
from typing import Any, Dict, Optional

class ConfigLoader:
    """Configuration loader with defaults for crypto wallet utility."""

    DEFAULTS: Dict[str, Any] = {
        "network": "mainnet",
        "rpc_endpoint": "https://mainnet.infura.io/v3/",
        "timeout_seconds": 30,
        "retry_count": 3,
        "log_level": "INFO",
        "storage_path": "./data/wallets",
        "gas_limit": 21000,
    }

    def __init__(self, config_path: Optional[str] = None) -> None:
        """Initialize the configuration loader."""
        self.config_path = config_path or "config.json"
        self._config: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        """Load configuration merging defaults, file and environment."""
        config = self.DEFAULTS.copy()

        # Load from file if it exists
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        config.update(file_data)
            except (json.JSONDecodeError, OSError):
                # Ignore invalid file, use defaults
                pass

        # Apply environment variable overrides
        for key in self.DEFAULTS:
            env_name = f"WALLET_UTILITY_{key.upper()}"
            if env_name in os.environ:
                env_value = os.environ[env_name]
                # Simple type conversion
                if env_value.isdigit():
                    config[key] = int(env_value)
                elif env_value.lower() in ("true", "false"):
                    config[key] = env_value.lower() == "true"
                else:
                    config[key] = env_value

        return config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value."""
        return self._config.get(key, default)

    def update(self, updates: Dict[str, Any]) -> None:
        """Update config values in memory."""
        self._config.update(updates)

    def save(self) -> bool:
        """Persist current config to the file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=4)
            return True
        except OSError:
            return False

    def __str__(self) -> str:
        return str(self._config)


def create_default_config(path: str = "config.json") -> None:
    """Create a config file with default values."""
    loader = ConfigLoader(path)
    loader.save()