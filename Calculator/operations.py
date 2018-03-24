"""Calculator.operations

Module that contains the math operations used by Calculator.
"""


def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """TODO: fill me in"""
    return a - b

def multiply(a, b):
    """TODO: fill me in"""
    return a * b

def divide(a, b):
    """TODO: fill me in"""
    # TODO: Add error if div by zero
    if b != 0:
        return float(a) / b

def abs_val(a):
    """TODO: fill me in"""
    if a < 0:
        return a*-1
    return a

def floor(a):
    """TODO: fill me in"""
    if a < 0:
        return int(a) - 1
    return int(a)

def ceiling(a):
    """TODO: fill me in"""
    if a < 0:
        return int(a)
    elif a % 1 == 0:
        return a
    return int(a) + 1

def power(a, b):
    """TODO: fill me in"""
    return a ** b

def rounding(a):
    """TODO: fill me in"""
    return int(a + 0.5)
