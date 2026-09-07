import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "gas_limit_multiplier": 1.15,
    "timeout_seconds": 30,
    "max_retries": 3,
    "cache_enabled": True,
    "log_level": "INFO",
}


class ConfigLoader:
    """Loads and manages wallet utility configuration with default fallbacks."""

    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        # Load settings from file if present
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass

        # Override with environment variables
        env_mappings = {
            "WALLET_NETWORK": ("network", str),
            "WALLET_RPC_URL": ("rpc_url", str),
            "WALLET_CHAIN_ID": ("chain_id", int),
            "WALLET_TIMEOUT": ("timeout_seconds", int),
            "WALLET_LOG_LEVEL": ("log_level", str),
        }

        for env_var, (config_key, cast_type) in env_mappings.items():
            value = os.getenv(env_var)
            if value is not None:
                try:
                    self._config[config_key] = cast_type(value)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Return full configuration dictionary."""
        return self._config.copy()


config = ConfigLoader()
