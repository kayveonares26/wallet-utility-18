import re
from typing import Union

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def wei_to_ether(wei_value: int) -> float:
    """Convert Wei to Ether value."""
    if wei_value < 0:
        raise ValueError("Wei value cannot be negative")
    return wei_value / 10**18


def ether_to_wei(ether_value: Union[int, float]) -> int:
    """Convert Ether to Wei value."""
    if ether_value < 0:
        raise ValueError("Ether value cannot be negative")
    return int(ether_value * 10**18)


def is_valid_eth_address(address: str) -> bool:
    """Check if the given string is a valid Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format wallet address for UI display by truncating the middle."""
    if not is_valid_eth_address(address):
        raise ValueError("Invalid Ethereum address format")
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"
