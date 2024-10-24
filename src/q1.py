def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap the values using arithmetic operations
    x = x + y
    y = x - y
    x = x - y
    
    print(f"Swapped values: x = {x}, y = {y}")
    return

# Task 2
# Invoke the function "swap" using the following scenarios:
print(swap("Apple", 10))  # Expected to return -1
print(swap(9, 17))        # Expected to print swapped values
