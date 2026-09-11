import re
from typing import Union

class ValidationError(ValueError):
    """Custom exception raised when crypto validation fails."""
    pass

def validate_ethereum_address(address: str) -> bool:
    """Validates an Ethereum address format.

    Args:
        address: The hex string representation of the address.

    Raises:
        ValidationError: If the address format is invalid.
    """
    if not isinstance(address, str):
        raise ValidationError("Address must be a string string representation")

    if not re.match(r"^(0x)?[0-9a-fA-F]{40}$", address):
        raise ValidationError("Address must be a 40-character hex string, optionally prefixed with 0x")
    return True

def validate_private_key(private_key: str) -> bool:
    """Validates a 256-bit private key in hexadecimal format.

    Args:
        private_key: The hex string representation of the private key.

    Raises:
        ValidationError: If the private key is mathematically or syntactically invalid.
    """
    if not isinstance(private_key, str):
        raise ValidationError("Private key must be a string")

    clean_key = private_key[2:] if private_key.startswith("0x") else private_key

    if not re.match(r"^[0-9a-fA-F]{64}$", clean_key):
        raise ValidationError("Private key must be a 64-character hexadecimal string")

    key_int = int(clean_key, 16)
    secp256k1_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

    if key_int == 0 or key_int >= secp256k1_order:
        raise ValidationError("Private key value is out of valid secp256k1 range")

    return True

def validate_transaction_amount(amount: Union[int, float, str]) -> int:
    """Validates and parses transaction amounts to prevent underflows or invalid types.

    Raises:
        ValidationError: If the transaction amount is non-positive or invalid.
    """
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise ValidationError("Amount must be a valid numeric type or numeric string")

    if val <= 0:
        raise ValidationError("Amount must be greater than zero")

    return int(val)