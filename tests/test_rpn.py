"""Brief description of what this file should test"""
import pytest

from Calculator import rpn

@pytest.mark.parametrize("equation, expected_result", [
    (["3" , "2", "*", "11" , "-"], -5.0),
    (["3","4","**", "2" , "3" , "-", "/"], -81.0),
])
def test_rpn_eval(equation, expected_result):
    assert rpn.rpn_eval(equation) == expected_result
