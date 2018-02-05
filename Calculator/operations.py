"""
Calculator.operations

Class that contains the math operations used by Calculator
"""


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return float(a) / b

    #To do: Add error if div by zero

def abs_val(a):
    if a < 0:
        return a*-1
    else:
        return a

def floor(a):
    if a<0:
        return int(a) - 1
    else:
        return int(a)

def ceiling(a):
    if a < 0:
        return int(a)
    elif a % 1 == 0:
        return a
    else:
        return int(a) + 1

def power(a,b):
        return a ** b

def rounding(a):
    return int(a + 0.5)
