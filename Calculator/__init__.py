"""Calculator

Base operations for a calculator
================================

tokenize
TokenError
_is_number
_is_symbol
_is_valid_character
"""

def tokenize(line):
    """Split the line into a list

    ``tokenize`` does not cover all error checking. It just chunks
    the string into a usable list for the rest of the program.

    Args:
        line (str): Math equation in the form of a string
    Returns:
        list: Tokens usable for evaluating
    """

    tokens = []
    number = ''

    line = line.strip()
    if not line:
        raise TokenError('No equation given')

    for char in line:

        if not _is_valid_character(char):
            raise TokenError('Invalid character: {}'.format(char))

        if _is_number(char):
            number += char

        elif _is_symbol(char):

            # two negatives make a positive
            if char == '-' and tokens and tokens[-1] == '-' and not number:
                tokens[-1] = '+'
                continue

            # append and reset
            if number:
                tokens.append(number)

            tokens.append(char)
            number = ''

        elif char == ' ':
            if number:
                tokens.append(number)
                number = ''

    if number:
        tokens.append(number)
    return tokens


def _is_number(char):
    """Check if a character is a valid number

    Valid characters:
        1234567890.

    Args:
        char (string): A single character
    Returns:
        bool: Whether a character is a number or not
    """

    return char.isdigit() or char == '.'


def _is_symbol(char):
    """Check if a character is a valid symbol

    Valid characters:
        +-*/()

    Args:
        char (string): A single character
    Returns:
        bool: Whether a character is a symbol or not
    """

    return char in ['+', '-', '*', '/', '(', ')']


def _is_valid_character(char):
    """Check if a character is valid in this math world

    Args:
        char (string): A single character
    Returns:
        bool: Whether a character is a parsable by this calculator or not
    """

    return _is_number(char) or _is_symbol(char) or char == ' '

class TokenError(Exception):
    pass
