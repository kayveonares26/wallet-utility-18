import re
from decimal import Decimal, InvalidOperation
from typing import Union

ETH_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
HEX_STR_REGEX = re.compile(r"^0x[a-fA-F0-9]+$")


class WalletValidationError(Exception):
    """Raised when wallet input or transaction parameter fails validation."""

    pass


def validate_crypto_address(address: str) -> str:
    """Validate EVM address structure and handle edge cases like whitespace and formatting."""
    if not isinstance(address, str):
        raise WalletValidationError("Address must be a string instance")

    cleaned = address.strip()
    if not cleaned:
        raise WalletValidationError("Address cannot be empty or whitespace")

    if not ETH_ADDRESS_REGEX.match(cleaned):
        raise WalletValidationError(f"Invalid EVM address format: '{address}'")

    return cleaned


def validate_transaction_amount(
    amount: Union[str, int, float],
    max_supply: int = 10**8,
) -> Decimal:
    """Parse and validate transaction amounts preventing floating point precision loss and overflow."""
    if amount is None:
        raise WalletValidationError("Amount cannot be None")

    try:
        # Prevent float precision truncation by coercing through precise string conversion
        str_val = str(amount) if not isinstance(amount, float) else f"{amount:.18f}"
        dec_amount = Decimal(str_val)
    except (InvalidOperation, TypeError, ValueError) as err:
        raise WalletValidationError(f"Invalid numeric format for transaction amount: {amount}") from err

    if dec_amount.is_nan() or dec_amount.is_infinite():
        raise WalletValidationError("Transaction amount cannot be NaN or Infinite")

    if dec_amount <= Decimal("0"):
        raise WalletValidationError("Transaction amount must be strictly greater than zero")

    if dec_amount > Decimal(max_supply):
        raise WalletValidationError(f"Amount exceeds maximum safety limit of {max_supply}")

    return dec_amount


def validate_hex_payload(payload: str, max_bytes: int = 131072) -> bytes:
    """Validate hex payload encoding, parity, and length boundaries."""
    if not isinstance(payload, str):
        raise WalletValidationError("Payload must be a hexadecimal string")

    cleaned = payload.strip()
    if not cleaned.startswith("0x") or not HEX_STR_REGEX.match(cleaned):
        raise WalletValidationError("Payload must be a valid 0x-prefixed hex string")

    clean_hex = cleaned[2:]
    if len(clean_hex) % 2 != 0:
        raise WalletValidationError("Hex payload contains an invalid odd number of characters")

    try:
        byte_data = bytes.fromhex(clean_hex)
    except ValueError as err:
        raise WalletValidationError("Failed to decode byte sequence from hex input") from err

    if len(byte_data) > max_bytes:
        raise WalletValidationError(f"Payload size ({len(byte_data)} bytes) exceeds max limit ({max_bytes} bytes)")

    return byte_data
