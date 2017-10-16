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
