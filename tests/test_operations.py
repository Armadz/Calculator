from Calculator import operations
from unittest import TestCase


class TestOperations(TestCase):

    def test_addition(self):
        assert operations.add(1,2) == 3

