from typing import Dict, Final, NamedTuple


class NetworkConfig(NamedTuple):
    chain_id: int
    symbol: str
    name: str
    derivation_path: str
    base_fee_gwei: int


# Supported Blockchain Networks
NETWORKS: Final[Dict[str, NetworkConfig]] = {
    "ethereum": NetworkConfig(
        chain_id=1,
        symbol="ETH",
        name="Ethereum Mainnet",
        derivation_path="m/44'/60'/0'/0/0",
        base_fee_gwei=20,
    ),
    "arbitrum": NetworkConfig(
        chain_id=42161,
        symbol="ETH",
        name="Arbitrum One",
        derivation_path="m/44'/60'/0'/0/0",
        base_fee_gwei=1,
    ),
    "optimism": NetworkConfig(
        chain_id=10,
        symbol="ETH",
        name="Optimism Mainnet",
        derivation_path="m/44'/60'/0'/0/0",
        base_fee_gwei=1,
    ),
    "polygon": NetworkConfig(
        chain_id=137,
        symbol="POL",
        name="Polygon Mainnet",
        derivation_path="m/44'/60'/0'/0/0",
        base_fee_gwei=30,
    ),
}

# Standard BIP-39 Wordlist Sizes
VALID_MNEMONIC_WORDS: Final[set[int]] = {12, 15, 18, 21, 24}

# Transaction priority levels and multipliers
GAS_MULTIPLIERS: Final[Dict[str, float]] = {
    "low": 1.0,
    "standard": 1.15,
    "fast": 1.3,
    "rapid": 1.5,
}

# Default API timeout in seconds
DEFAULT_TIMEOUT_SEC: Final[int] = 15
