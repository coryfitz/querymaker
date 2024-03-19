import inspect

def make_query(func):
    # Get the source code of the function
    source = inspect.getsource(func)
    # Split the source code into lines
    lines = source.splitlines()
    # Remove the first line (function definition)
    body_lines = lines[1:]
    # Initialize variables to store the modified body and the return line
    modified_body_lines = []
    return_line = ''
    for line in body_lines:
        # Strip leading whitespace from the line
        stripped_line = line.lstrip()
        # Replace 'if' with 'where'
        if 'if' in stripped_line:
            stripped_line = stripped_line.replace('if', 'WHERE')
        # Check if the line contains a return statement
        if stripped_line.startswith('return'):
            # Replace 'return' with 'select' and save it separately
            return_line = stripped_line.replace('return', 'SELECT', 1) + ' '
        else:
            # Add the modified line to the body lines
            modified_body_lines.append(stripped_line)
    # Concatenate the return line at the beginning and the rest of the body
    final_body = return_line + ' '.join(modified_body_lines)
    # Remove all colons from the final body
    final_body_no_colons = final_body.replace(':', '')
    return final_body_no_colons.strip() +';'