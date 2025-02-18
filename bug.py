def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct handling of a == 0
    if b == 0:
        return float('inf')  # Handle b == 0 to avoid ZeroDivisionError
    return a / b

result = function_with_uncommon_error(10, 0)