import re

def is_valid_address(address: str, chain: str = 'eth') -> bool:
    """Validate crypto wallet address format based on network type."""
    if chain == 'eth':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def is_valid_amount(amount: str) -> bool:
    """Verify that the provided amount is a positive decimal string."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def validate_transaction(data: dict) -> tuple[bool, str]:
    """Perform integrity checks on transaction payload dictionary."""
    required_fields = ['sender', 'recipient', 'amount']
    for field in required_fields:
        if field not in data:
            return False, f"missing required field: {field}"
    
    if not is_valid_address(data['sender']) or not is_valid_address(data['recipient']):
        return False, "invalid wallet address format"
    
    if not is_valid_amount(str(data['amount'])):
        return False, "invalid transaction amount"
    
    return True, "success"