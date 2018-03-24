"""Brief description of what this file should test"""

import pytest

from Calculator import operations


def test_addition():
    assert operations.add(1, 2) == 3

def test_subtraction():
    assert operations.subtract(1 ,2) == -1

def test_multiplication():
    assert operations.multiply(2, -1) == -2

def test_divide():
    # test for floating point division returns floating point
    assert isinstance(operations.divide(3, 2), float)
    assert operations.divide(8, 4) == 2
    # Check for div by zero
    assert operations.divide(1, 0) == None

@pytest.mark.parametrize("given, expected", [
    (0, 0),
    (-0.76, 0.76),
    (1, 1),
])
def test_abs_val(given, expected):
    assert operations.abs_val(given) == expected

@pytest.mark.parametrize("given, expected", [
    (0, 0),
    (.5, 0),
    (-0.75, -1),
])
def test_floor(given, expected):
    assert operations.floor(given) == expected

@pytest.mark.parametrize("given, expected", [
    (0, 0),
    (-1.5, -1),
    (2.3, 3),
])
def test_ceiling(given, expected):
    assert operations.ceiling(given) == expected

@pytest.mark.parametrize("given_a, given_b, expected", [
    (0, 1, 0),
    (3, 3, 27),
    (-3, 0, 1),
    (0, 0, 1),
])
def test_power(given_a, given_b, expected):
    assert operations.power(given_a, given_b) == expected

@pytest.mark.parametrize("given, expected", [
    (0.45, 0),
    (-3.6, -3),
    (3, 3),
])
def test_rounding(given, expected):
    assert operations.rounding(given) == expected
