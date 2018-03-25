"""calculator

Perform calculations on the command line
"""

import argparse

from Calculator import rpn_eval, tokenize


def main():
    """REPL style calculator

    REPL = Read-Evaluate-Print Loop
    """

    args = parse_args()

    # Read
    user_input = input('> ')

    while user_input != 'q':
        # Evaluate
        tokens = tokenize(user_input)
        if args.rpn:
            result = rpn_eval(user_input)
        else:
            # result = infix(user_input)
            pass

        # Print
        print(result)

        # Loop
        user_input = input('> ')

def parse_args():
    """Parse command line arguments

    Returns
        argparse.Namespace: Object that contains parsed args
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-r',
                        '--rpn',
                        default=False,
                        action='store_true',
                        help='Reverse Polish Notation (postfix notation)')
    return parser.parse_args()

if __name__ == '__main__':
    main()
