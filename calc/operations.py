# this function is for adding
def add(a, b):
    return a + b
# this function is for subtract
def subtract(a, b):
    return a - b
# this function is for multiply
def multiply(a, b):
    return a * b
# this function is for divide
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
