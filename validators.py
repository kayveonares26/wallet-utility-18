import re

def validate_wallet_address(address):
    """Validate Ethereum-style wallet address."""
    if not isinstance(address, str):
        return False
    # Check for 0x prefix and 40 hexadecimal characters
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount):
    """Validate positive transaction amount."""
    if not isinstance(amount, (int, float, str)):
        return False
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def validate_transaction(tx):
    """Validate transaction input data."""
    if not isinstance(tx, dict):
        return False
    if 'address' not in tx or 'amount' not in tx:
        return False
    return (validate_wallet_address(tx['address']) and 
            validate_amount(tx['amount']))

def main_processing_loop(transactions):
    """Main processing loop with input validation."""
    valid_count = 0
    invalid_count = 0
    for tx in transactions:
        if validate_transaction(tx):
            # Process the valid transaction
            print(f"Processing tx: address={tx['address']}, amount={tx['amount']}")
            valid_count += 1
        else:
            print(f"Skipping invalid input: {tx}")
            invalid_count += 1
    print(f"Summary: {valid_count} valid, {invalid_count} invalid")
    return valid_count, invalid_count

if __name__ == "__main__":
    samples = [
        {"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": "100.5"},
        {"address": "0x1234567890123456789012345678901234567890", "amount": "0"},
        {"address": "invalidaddress", "amount": "50"},
        {"address": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd", "amount": 25},
    ]
    main_processing_loop(samples)