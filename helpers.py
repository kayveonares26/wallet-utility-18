import decimal
from typing import Union

def normalize_amount(amount: Union[str, float, int]) -> decimal.Decimal:
    """Converts various input types to a standardized Decimal format."""
    try:
        return decimal.Decimal(str(amount)).quantize(decimal.Decimal('0.00000001'), rounding=decimal.ROUND_HALF_UP)
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0.0')

def format_crypto_address(address: str) -> str:
    """Sanitizes address strings by stripping whitespace and casing."""
    if not address:
        return ""
    return address.strip().lower()

def validate_fee_rate(fee_rate: float) -> bool:
    """Checks if provided fee rate is within acceptable network bounds."""
    MIN_FEE = 0.00000001
    MAX_FEE = 0.1
    return MIN_FEE <= fee_rate <= MAX_FEE

def mask_private_key(key: str) -> str:
    """Redacts sensitive key data for logging security."""
    if len(key) < 8:
        return "***"
    return f"{key[:4]}...{key[-4:]}"