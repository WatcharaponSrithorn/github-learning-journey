def add(a, b):
    result = a+b
    return result

def subtract(a, b):
    result = a-b
    return result

def multiply(a, b):
    result = a*b
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = a/b
    return result

if __name__ == "__main__":
    print(add(2, 3))        # Output: 5
    print(subtract(5, 2))   # Output: 3
    print(multiply(4, 3))   # Output: 12
    print(divide(10, 2))    # Output: 5.0
    print(divide(10, 0))    # Output: Error: Division by zero is not allowed.