"""
This module contains the functions used by Calculator program 
to change infix notation into postfix notation
"""
import numbers
output = []
operation_stack = []

def op_precedence(operation):
    """Checks the precednece of an operations
    
    Args:
        operation (str): mathematical operator

    Renturns:
        int: Precednece of the operation
    """

    return {
            '(': 6,
            '^': 4,
            '*': 3,
            '/': 3,
            '-': 2,
            '+': 2,
    }[operation]

def assoc_is_left(operation):
    """Checks if an operations assocativity is left

    Args:
        Operator (str): Mathematical operator
    Returns:
        Boolean: True if Assocativity is left
    """

    return {
            '(': False,
            '^': False,
            '*': True,
            '/': True, 
            '-': True,
            '+': True,
    }[operation]

def op_switch(i, j):
    """Checks for the conditions to activate the shunt

    Args:
        i (str): incoming operator for tokens
        j (str): Operator at the Top of the operation Stack
    Returns:
        Boolean: if conditions are met shuntingswitch is True
    """
    
    if j != '(':
        if op_precedence(j) > op_precedence(i):
            return True
        elif op_precedence(j) == op_precedence(i) and \
                assoc_is_left(j):
            return True
        else:
            return False
    else:
        return False

def shuntingyard(eq):
    """Transforms infix equations to rpn equations

    Args:
        eq (list): processed infix equation
    Returns:
        output (lists): rpn equation
    """

    for i in eq:
        if isinstance(i, numbers.Real):
            output.append(i)
        elif i in [ '^', '*', '/', '-', '+']:
            if operation_stack:
                while op_switch(i, operation_stack[-1]) and operation_stack:
                    output.append(operation_stack.pop())
            operation_stack.append(i)
        elif i == '(':
            operation_stack.append(i)
        elif i == ')':
            while operation_stack[-1] != '(':
                output.append(operation_stack.pop())
            operation_stack.pop()
    while operation_stack:
        output.append(operation_stack.pop())
    return output[:]
