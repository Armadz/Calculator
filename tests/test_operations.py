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

    def test_abs_val(self):
        assert operations.abs_val(0) == 0
        assert operations.abs_val(-0.76) == 0.76
        assert operations.abs_val(1) == 1

    def test_floor(self):
        assert operations.floor(0) == 0
        assert operations.floor(.5) == 0
        assert operations.floor(-0.75) == -1

    def test_ceiling(self):
        assert operations.ceiling(0) == 0
        assert operations.ceiling(-1.5) == -1
        assert operations.ceiling(2.3) == 3



    def test_power(self):
        assert operations.power(0,1) == 0
        assert operations.power(3,3) == 27
        assert operations.power(-3, 0) == 1
        assert operations.power(0,0) == None


    def test_rounding(self):
        assert operations.rounding(0.45) == 0
        assert operations.rounding(-3.6) == -3
        assert operations.rounding(3) == 3
