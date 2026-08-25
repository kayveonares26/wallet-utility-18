import os
import json
from typing import Any, Dict, Optional

DEFAULTS = {
    "network": "mainnet",
    "rpc_url": "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
    "chain_id": 1,
    "gas_price_gwei": 20,
    "timeout": 30,
    "max_retries": 3,
    "log_level": "INFO",
    "wallet_dir": "./data/wallets",
    "use_encryption": True,
    "api_key": ""
}

class ConfigurationLoader:
    """Loads wallet configuration using defaults, JSON file and environment variables."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = config_path or os.getenv("WALLET_UTILITY_CONFIG", "config.json")
        self.config: Dict[str, Any] = DEFAULTS.copy()
        self._load_from_file()
        self._apply_environment_overrides()

    def _load_from_file(self) -> None:
        """Load and merge config from JSON file if present."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                if isinstance(file_config, dict):
                    self.config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass

    def _apply_environment_overrides(self) -> None:
        """Apply overrides from environment variables prefixed with WALLET_."""
        prefix = "WALLET_"
        for key, default_value in DEFAULTS.items():
            env_var = prefix + key.upper()
            if env_var in os.environ:
                env_value = os.environ[env_var]
                if isinstance(default_value, bool):
                    self.config[key] = env_value.lower() in ("true", "1", "yes", "on")
                elif isinstance(default_value, int):
                    try:
                        self.config[key] = int(env_value)
                    except ValueError:
                        self.config[key] = default_value
                else:
                    self.config[key] = env_value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve configuration value or default."""
        return self.config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """Return a copy of the full configuration."""
        return self.config.copy()