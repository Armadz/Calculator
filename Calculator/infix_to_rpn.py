"""
This module contains the functions used by Calculator program 
to change infix notation into postfix notation
"""

output = []
operation_stack = []

def op_precedence(operation):
    return {
            '(': 6,
            '^': 4,
            '*': 3,
            '/': 3,
            '-': 2,
            '+': 2,
    }[operation]

def assoc_is_left(operation):
    return {
            '(': False,
            '^': False,
            '*': True,
            '/': True, 
            '-': True,
            '+': True,
    }[operation]

def op_switch(i, j):
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
    for i in eq:
        if i is float:
            output.append(i)
            continue
        elif i in [ '^', '*', '/', '-', '+' ]:
            while op_switch(i, operation_stack[-1]) and operation_stack:
                output.append(operation_stack.pop())
            operation_stack.append(i)
        elif i == '(':
            operation_stack.append(i)
        elif i == ')':
            while operation_stack[-1] != '(':
                output.append(operation_stack.pop())
            operation_stack.pop
    while operation_stack:
        output.append(oepration_stack.pop())
    return output[:]
