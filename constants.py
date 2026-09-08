from enum import Enum
from typing import Dict, Final

class CryptoNetwork(Enum):
    BITCOIN = "BTC"
    ETHEREUM = "ETH"
    SOLANA = "SOL"

# Standard precision mapping for crypto assets
ASSET_PRECISION: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "SOL": 9,
    "USDC": 6,
    "USDT": 6
}

# Network-specific explorer endpoints
EXPLORER_URLS: Final[Dict[CryptoNetwork, str]] = {
    CryptoNetwork.BITCOIN: "https://blockstream.info",
    CryptoNetwork.ETHEREUM: "https://etherscan.io",
    CryptoNetwork.SOLANA: "https://explorer.solana.com"
}

# Transaction confirmation thresholds
MIN_CONFIRMATIONS: Final[Dict[CryptoNetwork, int]] = {
    CryptoNetwork.BITCOIN: 2,
    CryptoNetwork.ETHEREUM: 12,
    CryptoNetwork.SOLANA: 1
}

def get_precision(symbol: str) -> int:
    """Return the decimal precision for a given ticker."""
    return ASSET_PRECISION.get(symbol.upper(), 8)

def is_supported(network: str) -> bool:
    """Check if the provided network is supported."""
    return network.upper() in [n.value for n in CryptoNetwork]