import os
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class NetworkConfig:
    mainnet_rpc: str = "https://mainnet.infura.io/v3/"
    testnet_rpc: str = "https://sepolia.infura.io/v3/"
    timeout: int = 30

def load_environment_config() -> Dict[str, Any]:
    """Extract sensitive wallet settings from system environment"""
    return {
        "rpc_url": os.getenv("RPC_URL", NetworkConfig.mainnet_rpc),
        "api_key": os.getenv("WALLET_API_KEY", ""),
        "timeout": int(os.getenv("REQUEST_TIMEOUT", NetworkConfig.timeout)),
        "debug": os.getenv("DEBUG_MODE", "false").lower() == "true"
    }

# Global config instance for application lifecycle
settings = load_environment_config()