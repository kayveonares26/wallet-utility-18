# Error handling helpers for crypto wallet edge cases
import json
import re
from typing import Any, Dict

def validate_wallet_address(address: str) -> bool:
    if not address or not isinstance(address, str):
        raise ValueError("Address must be a non-empty string")
    if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
        raise ValueError("Invalid wallet address format")
    return True

def calculate_transaction_fee(balance: float, fee_rate: float) -> float:
    if balance <= 0:
        raise ValueError("Balance must be positive")
    if not (0 <= fee_rate <= 1):
        raise ValueError("Fee rate must be between 0 and 1")
    fee = balance * fee_rate
    if fee > balance:
        raise ValueError("Calculated fee exceeds available balance")
    return fee

def parse_transaction_data(data: str) -> Dict[str, Any]:
    if not data or not isinstance(data, str):
        raise ValueError("Transaction data must be a non-empty string")
    try:
        parsed = json.loads(data)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in transaction data: {str(exc)}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("Transaction data must parse to a dictionary")
    required = ["to", "amount", "from"]
    missing = [f for f in required if f not in parsed]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    return parsed

def process_wallet_request(operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if operation not in ["send", "balance", "validate"]:
        raise ValueError("Unsupported wallet operation")
    try:
        if operation == "validate":
            if "address" not in params:
                raise ValueError("Address parameter is required")
            validate_wallet_address(params["address"])
            return {"status": "success", "valid": True}
        elif operation == "send":
            if "data" not in params or "balance" not in params or "fee_rate" not in params:
                raise ValueError("Required parameters missing for send operation")
            tx = parse_transaction_data(params["data"])
            fee = calculate_transaction_fee(params["balance"], params["fee_rate"])
            return {"status": "success", "transaction": tx, "fee": fee}
        elif operation == "balance":
            if "balance" not in params:
                raise ValueError("Balance parameter is required")
            bal = params["balance"]
            if not isinstance(bal, (int, float)) or bal < 0:
                raise ValueError("Balance must be a non-negative number")
            return {"status": "success", "balance": bal}
    except ValueError as ve:
        return {"status": "error", "message": str(ve)}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}
    return {"status": "error", "message": "Operation not handled"}