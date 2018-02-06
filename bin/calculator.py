"""calculator

Perform calculations on the command line
"""

import argparse

from Calculator import (
    tokenize,
    TokenError,
)
from Calculator.rpn import rpn_eval

def main():
    """Main function"""

    args = parse_args()

    user_input = ''
    while user_input != 'q':
        user_input = input(args.prompt)
        if user_input == 'q':
            print('Exiting...')
            continue

        try:
            tokens = tokenize(user_input)
        except TokenError as err:
            print(err)
            continue

        if args.rpn:
            # Do RPN calculation
            print(rpn_eval(tokens))
        else:
            # do infix calculation
            # infix(user_input)
            pass

def parse_args():
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-r',
                        '--rpn',
                        default=False,
                        action='store_true',
                        help='Reverse Polish Notation (postfix notation)')
    parser.add_argument('-p',
                        '--prompt',
                        default='> ',
                        help='What the repl prompt looks like')
    return parser.parse_args()

if __name__ == '__main__':
    main()
