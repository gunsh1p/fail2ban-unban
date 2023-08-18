def parse_args(string):
    args = []
    current_arg = ''
    in_quotes = False
    
    for char in string:
        if char == ' ' and not in_quotes:
            if current_arg:
                if current_arg.isdigit():
                    current_arg = int(current_arg)
                elif current_arg.replace('.', '', 1).isdigit():
                    current_arg = float(current_arg)
                args.append(current_arg)
                current_arg = ''
        elif char == '"':
            in_quotes = not in_quotes
        else:
            current_arg += char
    
    if current_arg:
        if current_arg.isdigit():
            current_arg = int(current_arg)
        elif current_arg.replace('.', '', 1).isdigit():
            current_arg = float(current_arg)
        args.append(current_arg)
    
    return args