import re
from typing import Union

SATOSHI_PER_BTC = 100_000_000
WEI_PER_ETH = 10**18


def satoshi_to_btc(satoshi: int) -> float:
    """Convert Satoshi amount to Bitcoin (BTC)."""
    if satoshi < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return satoshi / SATOSHI_PER_BTC


def btc_to_satoshi(btc: Union[int, float]) -> int:
    """Convert Bitcoin (BTC) amount to Satoshi."""
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(round(btc * SATOSHI_PER_BTC))


def wei_to_eth(wei: int) -> float:
    """Convert Wei amount to Ether (ETH)."""
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei / WEI_PER_ETH


def eth_to_wei(eth: Union[int, float]) -> int:
    """Convert Ether (ETH) amount to Wei."""
    if eth < 0:
        raise ValueError("ETH amount cannot be negative")
    return int(round(eth * WEI_PER_ETH))


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format wallet address for display (e.g., 0x1234...abcd)."""
    if not address:
        return ""
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"
