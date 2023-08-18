def is_ipv4(string: str) -> bool:
    # Split the string into its four octets
    octets = string.split('.')
    
    # Check if there are exactly four octets
    if len(octets) != 4:
        return False
    
    # Check if each octet is an integer between 0 and 255
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    
    return True