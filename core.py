import decimal
from typing import Union

# Set precision for crypto calculations
decimal.getcontext().prec = 18

def format_crypto_amount(amount: Union[str, float, int], decimals: int = 8) -> str:
    """
    Normalizes crypto amounts to standard string representation.
    Handles floating point issues by utilizing decimal library.
    """
    try:
        d_amount = decimal.Decimal(str(amount))
        # Truncate to desired decimal places without rounding
        factor = decimal.Decimal(10) ** decimals
        normalized = (d_amount * factor).to_integral_value(rounding=decimal.ROUND_DOWN) / factor
        return f"{normalized:.{decimals}f}"
    except (decimal.InvalidOperation, ValueError):
        return "0.00000000"

def calculate_fee(amount: str, fee_rate: float) -> str:
    """
    Computes transaction fee based on amount and rate.
    Returns string for precision consistency.
    """
    amount_dec = decimal.Decimal(amount)
    fee = amount_dec * decimal.Decimal(str(fee_rate))
    return format_crypto_amount(fee)

def validate_address_format(address: str, chain_prefix: str = "0x") -> bool:
    """
    Basic hex-based address validation for evm chains.
    """
    if not address.startswith(chain_prefix):
        return False
    hex_part = address[len(chain_prefix):]
    return len(hex_part) == 40 and all(c in "0123456789abcdefABCDEF" for c in hex_part)