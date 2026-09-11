import sys
from typing import Final, Dict

# Network identifier constants for blockchain protocols
# Using dictionary lookups for O(1) performance

MAINNET_ID: Final[str] = "mainnet"
TESTNET_ID: Final[str] = "testnet"

# Cached configuration constants for reduced lookup overhead
NETWORKS: Final[Dict[str, str]] = {
    "ETH": "ethereum",
    "BTC": "bitcoin",
    "SOL": "solana",
    "DOT": "polkadot"
}

# Transaction threshold limits
MIN_TX_FEE: Final[float] = 0.00001
MAX_TX_RETRY_COUNT: Final[int] = 3

# Formatting constants to optimize string concatenation operations
DECIMAL_PRECISION: Final[int] = 8
CURRENCY_SYMBOL: Final[str] = "$"

def get_network_name(ticker: str) -> str:
    """Return network name from cache map."""
    return NETWORKS.get(ticker.upper(), "unknown")

# Memory-mapped buffer sizes for batch processing
BUFFER_SIZE_BYTES: Final[int] = 1024 * 64

if __name__ == "__main__":
    # Basic smoke test for constant access performance
    print(f"Active network mapping size: {len(NETWORKS)}")