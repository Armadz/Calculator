"""calculator

Perform calculations on the command line
"""

import argparse

def main():
    """Main function"""

    args = parse_args()

    user_input = None
    while user_input != 'q':

        user_input = input('> ')
        if args.rpn:
            # Do RPN calculation
            # rpn(user_input)
            pass
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
    return parser.parse_args()

if __name__ == '__main__':
    main()
