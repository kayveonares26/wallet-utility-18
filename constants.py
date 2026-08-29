"""Performance optimized constants for crypto wallet utility."""
import functools
from typing import Dict, Optional

SUPPORTED_CHAINS: Dict[str, int] = {
    "ethereum": 1,
    "bitcoin": 0,
    "binance": 56,
    "polygon": 137,
    "arbitrum": 42161,
}

DEFAULT_GAS_PRICES: Dict[str, int] = {
    "ethereum": 20000000000,
    "polygon": 30000000000,
    "binance": 5000000000,
}

TOKEN_DECIMALS: Dict[str, int] = {
    "ETH": 18,
    "BTC": 8,
    "USDT": 6,
    "USDC": 6,
}

@functools.lru_cache(maxsize=128)
def get_chain_id(chain: str) -> Optional[int]:
    return SUPPORTED_CHAINS.get(chain.lower())

@functools.lru_cache(maxsize=128)
def get_gas_price(chain: str) -> Optional[int]:
    return DEFAULT_GAS_PRICES.get(chain.lower())

@functools.lru_cache(maxsize=128)
def get_token_decimals(token: str) -> Optional[int]:
    return TOKEN_DECIMALS.get(token.upper())

class WalletConstants:
    __slots__ = ('chains', 'gas_prices', 'decimals')
    def __init__(self):
        self.chains = SUPPORTED_CHAINS
        self.gas_prices = DEFAULT_GAS_PRICES
        self.decimals = TOKEN_DECIMALS
    def get_chain_id(self, chain: str) -> Optional[int]:
        return self.chains.get(chain.lower())
    def get_gas_price(self, chain: str) -> Optional[int]:
        return self.gas_prices.get(chain.lower())
    def get_decimals(self, token: str) -> Optional[int]:
        return self.decimals.get(token.upper())
    def convert_to_base_unit(self, amount: float, token: str) -> int:
        dec = self.get_decimals(token) or 18
        return int(amount * (10 ** dec))

WALLET_CONSTANTS = WalletConstants()