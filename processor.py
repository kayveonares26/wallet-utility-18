from decimal import Decimal, InvalidOperation
from typing import Optional, Dict, Any

# wallet-utility-18: core crypto data sanitization

def normalize_amount(amount: Any) -> Decimal:
    """Converts various input types to a standardized Decimal."""
    try:
        if isinstance(amount, float):
            return Decimal(str(amount))
        return Decimal(amount)
    except (InvalidOperation, ValueError, TypeError):
        return Decimal('0.0')

def format_balance(balance: Decimal, decimals: int = 8) -> str:
    """Formats precise crypto balances for display."""
    return f"{balance:.{decimals}f}"

def parse_transaction_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts and cleans fields from exchange payloads."""
    return {
        "tx_id": str(raw_data.get("hash", "")), 
        "value": normalize_amount(raw_data.get("value", 0)),
        "asset": str(raw_data.get("symbol", "UNKNOWN")).upper(),
        "valid": bool(raw_data.get("confirmed", False))
    }

if __name__ == "__main__":
    # usage demonstration for dev testing
    test_payload = {"hash": "0xabc123", "value": "0.005", "symbol": "eth", "confirmed": True}
    print(parse_transaction_data(test_payload))