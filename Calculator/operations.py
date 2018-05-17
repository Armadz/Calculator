"""Calculator.operations

Module that contains the math operations used by Calculator.
"""


def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides two number, raises an error if div by zero"""
    if b != 0:
        return float(a) / b
    elif b == 0:
        raise DivisionByZeroError('Division by Zero is undefined')

def abs_val(a):
    """Returns the absolute value of a number"""
    if a < 0:
        return a*-1
    return a

def floor(a):
    """Returns the floor value of a number"""
    if a < 0:
        return int(a) - 1
    return int(a)

def ceiling(a):
    """Returns the ceiling value of a number"""
    if a < 0:
        return int(a)
    elif a % 1 == 0:
        return a
    return int(a) + 1

def power(a, b):
    """Raises the first number to the power of the second number"""
    return a ** b

def rounding(a):
    """Rounds a number to the nearest interger value"""
    return int(a + 0.5)

class DivisionByZeroError(Exception):
    """Execption for Division by zero"""
    pass
