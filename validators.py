import re

# regex patterns for crypto validation
ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_wallet_address(address: str) -> bool:
    """Checks if provided string is a valid hex-based wallet address."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and finite."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def process_input_validation(data: dict) -> bool:
    """Main validation gate for incoming transaction payloads."""
    required_fields = ['address', 'amount', 'currency']
    if not all(k in data for k in required_fields):
        return False
    
    if not validate_wallet_address(data['address']):
        return False
        
    if not validate_amount(data['amount']):
        return False
        
    return True