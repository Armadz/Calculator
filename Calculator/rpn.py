"""

Class that contains the function for evaluating a list of strings in Reverse Polish Notation
"""

from Calculator import operations



def rpn_eval(eq):
    operations_switch = {
        '+':operations.add,
        '-':operations.subtract,
        '*':operations.multiply,
        "/":operations.divide,
        "**":operations.power
    }
    evstack = []
    for i in eq:
        if i in operations_switch:
                b = evstack.pop()
                a = evstack.pop()
                n = operations_switch[i](a,b)
                evstack.append(n)
        else:
            n = float(i)
            evstack.append(n)

    return evstack.pop()
