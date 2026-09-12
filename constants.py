import os
from typing import Dict

# Network identifiers
NETWORKS: Dict[str, str] = {
    "mainnet": "https://mainnet.infura.io/v3/",
    "sepolia": "https://sepolia.infura.io/v3/",
}

# Transaction constants
DEFAULT_GAS_LIMIT: int = 21000
MAX_RETRIES: int = 3
TIMEOUT_SECONDS: int = 30

# Application paths
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: str = os.path.join(BASE_DIR, "logs")

# Crypto asset identifiers
SUPPORTED_TOKENS = {
    "ETH": "0x0000000000000000000000000000000000000000",
    "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
}

# Security settings
MIN_PASSWORD_LENGTH: int = 12
PBKDF2_ITERATIONS: int = 600000