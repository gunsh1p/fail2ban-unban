def parse_args(string: str) -> list:
    args = []
    current_arg = ''
    in_quotes = False
    
    for char in string:
        if char == ' ' and not in_quotes:
            if current_arg:
                args.append(current_arg)
                current_arg = ''
        elif char == '"':
            in_quotes = not in_quotes
        else:
            current_arg += char
    
    if current_arg:
        args.append(current_arg)
    
    return args