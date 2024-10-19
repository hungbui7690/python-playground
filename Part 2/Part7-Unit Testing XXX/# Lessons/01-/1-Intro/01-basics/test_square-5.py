"""
Testing expected exceptions

"""

import unittest
from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square("10")

    # The following example adds a test that expects a ValueError exception if the length is zero or negative:
    def test_length_with_zero_or_negative(self):
        with self.assertRaises(ValueError):
            square = Square(0)
            square = Square(-1)


# 1. If you run the test, it’ll fail:
# python -m unittest -v

# ======================================================================
# FAIL: test_length_with_zero_or_negative (test_square.TestSquare.test_length_with_zero_or_negative)
# ----------------------------------------------------------------------
# AssertionError: ValueError not raised
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.002s
#
# FAILED (failures=2)


# 2. To make the test pass, you add another check to the Square() constructor: square-5.py
# Now, all three tests pass:
# python -m unittest -v

# test_area (test_square.TestSquare.test_area) ... ok
# test_length_with_wrong_type (test_square.TestSquare.test_length_with_wrong_type) ... ok
# test_length_with_zero_or_negative (test_square.TestSquare.test_length_with_zero_or_negative) ... ok
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s
#
# OK


# Summary
# A unit test is an automated test that verifies a small piece of code, executes fast, and executes in an isolated manner.
# Use the unittest module to perform unit testing.
# Create a class that inherits from the unittest.TestCase class to make a test case.
# Use the assertEqual() method to test if two values are equal.
# Use the assertRaises() method in a context manager to test expected exceptions.
# Use the python -m unittest -v command to run a test.
