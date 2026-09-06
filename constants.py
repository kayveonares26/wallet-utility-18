import os
from typing import Final

# Network identifiers
MAINNET: Final[str] = 'mainnet'
TESTNET: Final[str] = 'testnet'

# Default connection settings
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Wallet storage configuration
STORAGE_DIR: Final[str] = os.getenv('WALLET_DATA_DIR', './data')
KEYSTORE_PATH: Final[str] = os.path.join(STORAGE_DIR, 'keystore.json')

# API limits and pricing
RATE_LIMIT_PER_MINUTE: Final[int] = 60
GAS_PRICE_DEFAULT: Final[int] = 20000000000

# Supported protocols
SUPPORTED_NETWORKS: Final[tuple] = (MAINNET, TESTNET)

# Encryption settings
KDF_ITERATIONS: Final[int] = 262144
ALGORITHM: Final[str] = 'aes-256-gcm'

# Logging configuration
LOG_LEVEL: Final[str] = 'INFO'
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'