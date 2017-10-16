from Calculator import operations
from unittest import TestCase


class TestOperations(TestCase):

    def test_addition(self):
        assert operations.add(1,2) == 3

    def test_subtraction(self):
        assert operations.subtract(1,2) == -1

    def test_multiplication(self):
        assert operations.multiply(2,-1) == -2

    def test_divide(self):
        #test for floating point division returns floating point
        assert type(operations.divide(3,2)) == float
        assert operations.divide(8,4) == 2
        #Check for div by zero
        assert operations.divide(1,0) == None
    
