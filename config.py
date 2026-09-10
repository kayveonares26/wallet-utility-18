import os
import json
from typing import Any, Dict

# Sensible default parameters for the crypto wallet interface
DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "timeout_seconds": 30,
    "max_retries": 3,
    "gas_multiplier": 1.15,
    "enable_cache": True
}

class WalletConfig:
    """Manages loading of application configuration with fallback defaults and environment overrides."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self) -> None:
        """Reads configuration from disk and parses wallet-specific environment variables."""
        # Load settings from a configuration file if it exists
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.settings.update(file_config)
            except (json.JSONDecodeError, IOError):
                pass  # Fall back to default config if reading fails

        # Override config parameters using standard WALLET_ prefix env vars
        for key in DEFAULT_CONFIG.keys():
            env_key = f"WALLET_{key.upper()}"
            env_value = os.getenv(env_key)
            if env_value is not None:
                default_val = DEFAULT_CONFIG[key]
                try:
                    if isinstance(default_val, bool):
                        self.settings[key] = env_value.lower() in ("true", "1", "yes")
                    elif isinstance(default_val, int):
                        self.settings[key] = int(env_value)
                    elif isinstance(default_val, float):
                        self.settings[key] = float(env_value)
                    else:
                        self.settings[key] = env_value
                except ValueError:
                    pass  # Keep current value if type casting fails

    def get(self, key: str) -> Any:
        """Retrieves config parameter value with fallback to global default."""
        return self.settings.get(key, DEFAULT_CONFIG.get(key))