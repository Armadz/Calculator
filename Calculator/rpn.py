"""Calculator.rpn

Module that contains the function for evaluating a list of strings
in Reverse Polish Notation.
"""

from Calculator import operations



def rpn_eval(equation):
    """Reverse Polish Notation evaluation

    Calculate the result of a calculation in RPN form.

    Args:
        equation (list): tokenized equation ordered in postfix notation

    Returns:
        int: result of an equation
    """

    operations_switch = {
        '+': operations.add,
        '-': operations.subtract,
        '*': operations.multiply,
        "/": operations.divide,
        "**": operations.power
    }

    eval_stack = []
    for value in equation:
        if value in operations_switch:
            b = eval_stack.pop()
            a = eval_stack.pop()
            number = operations_switch[value](a, b)
        else:
            number = float(value)

        eval_stack.append(number)

    return eval_stack.pop()
