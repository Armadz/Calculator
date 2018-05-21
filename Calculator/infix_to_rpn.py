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

def op_switch(token, top_of_op_stack):
    """Checks for the conditions to activate the shunt

    Args:
        token (str): incoming operator for tokens
        top_of_op_stack (str): Operator at the Top of the operation Stack
    Returns:
        Boolean: if conditions are met shuntingswitch is True
    """
    
    if top_of_op_stack != '(':
        if op_precedence(top_of_op_stack) > op_precedence(token):
            return True
        elif op_precedence(top_of_op_stack) == op_precedence(token) and \
                assoc_is_left(top_of_op_stack):
            return True
        else:
            return False
    else:
        return False

def shuntingyard(tokens):
    """Transforms infix equations to rpn equations

    Args:
        tokens (list): processed infix equation
    Returns:
        output (lists): rpn equation
    """

    for token in tokens:
        if isinstance(token, numbers.Real):
            output.append(token)
        elif token in [ '^', '*', '/', '-', '+']:
            if operation_stack:
                while op_switch(token, operation_stack[-1]) and operation_stack:
                    output.append(operation_stack.pop())
            operation_stack.append(token)
        elif token == '(':
            operation_stack.append(token)
        elif token == ')':
            while operation_stack[-1] != '(':
                output.append(operation_stack.pop())
            operation_stack.pop()
    while operation_stack:
        output.append(operation_stack.pop())
    return output[:]
