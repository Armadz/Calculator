from Calculator import rpn
from unittest import TestCase

class TestRPN(TestCase):

    def test_rpn_eval(self):
        assert rpn.rpn_eval(["3" , "2", "*", "11" , "-"]) == -5.0

    def test_rpn_powers(self):
        assert rpn.rpn_eval(["3","4","**", "2" , "3" , "-", "/"])==-81.0
