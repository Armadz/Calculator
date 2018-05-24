from Calculator import infix_to_rpn

import pytest

@pytest.mark.parametrize('test_input, expected', [
        ('+', 2),
        ('*', 3),
        ('^', 4),
])
def test_op_precedence(test_input, expected):
    assert infix_to_rpn.op_precedence(test_input) == expected

@pytest.mark.parametrize('test_input, expected', [
        ('+', True),
        ('*', True),
        ('^', False),
])
def test_assoc_is_left(test_input, expected):
    assert infix_to_rpn.assoc_is_left(test_input) == expected

@pytest.mark.parametrize('test_input_1, test_input_2, expected', [
        ('+', '-', True),
        ('*', '-', False),
        ('-', '^', True),
        ('*', '(', False),
])
def test_op_switch(test_input_1, test_input_2, expected):
    assert infix_to_rpn.op_switch(test_input_1, test_input_2) == expected

@pytest.mark.parametrize('test_input, expected', [
        ([ '3' , '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2',
	'^', '3'], ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/',
	'+']),
])
def test_shuntingyard(test_input, expected):
    assert infix_to_rpn.shuntingyard(test_input) == expected
