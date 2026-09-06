import re

# Configuration for crypto address formats
ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

def validate_input(data):
    """Ensures wallet input meets checksum or length requirements."""
    if not isinstance(data, str):
        return False
    return bool(ADDRESS_PATTERN.match(data))

def process_wallet_batch(wallets):
    """Main processing loop with integrated input validation."""
    valid_addresses = []
    errors = []

    for entry in wallets:
        # Scrub input before processing
        clean_address = entry.strip()

        if validate_input(clean_address):
            valid_addresses.append(clean_address)
        else:
            errors.append(f"invalid address format: {clean_address}")
            
    return valid_addresses, errors

if __name__ == '__main__':
    # Simulation of incoming batch
    test_batch = ['0x1234567890abcdef1234567890abcdef12345678', 'invalid_entry', 'abc123']
    processed, failed = process_wallet_batch(test_batch)
    
    print(f"Processed: {len(processed)} items")
    if failed:
        print(f"Errors encountered: {', '.join(failed)}")