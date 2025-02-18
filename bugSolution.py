def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct handling of a == 0
    if b == 0:
        return float('inf')  # Handle b == 0 to avoid ZeroDivisionError
    return float(a) / float(b) #Explicit type conversion to float

result = function_with_uncommon_error(10, 0)
print(result) #Output: inf
result = function_with_uncommon_error(10,2)
print(result) #Output: 5.0