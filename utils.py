import hashlib
from typing import Optional

def generate_address_checksum(public_key_hex: str) -> str:
    """
    Generates a checksum for a given hex-encoded public key.
    
    Args:
        public_key_hex: The hexadecimal string representation of the public key.

    Returns:
        A string representing the checksummed address.
    """
    key_bytes = bytes.fromhex(public_key_hex)
    hash_result = hashlib.sha256(key_bytes).hexdigest()
    return f"0x{hash_result[:40]}"

def validate_transaction_fee(fee_amount: float, minimum_fee: float = 0.0001) -> bool:
    """
    Checks if the provided transaction fee meets the minimum requirements.

    Args:
        fee_amount: The proposed fee to be paid for the transaction.
        minimum_fee: The minimum required fee (default 0.0001).

    Returns:
        True if fee is acceptable, False otherwise.
    """
    return fee_amount >= minimum_fee

def format_wei_to_eth(wei_value: int) -> float:
    """
    Converts a balance from Wei to Ether.

    Args:
        wei_value: The balance in Wei.

    Returns:
        The balance in Ether as a float.
    """
    return wei_value / 10**18