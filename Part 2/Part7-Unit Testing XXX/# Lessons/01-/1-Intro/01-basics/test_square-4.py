"""
Testing expected exceptions

- The Square constructor accepts a length parameter. The length parameter should be either an int or float. If you pass the value that is not in these types, the Square constructor should raise a TypeError exception.

"""

import unittest
from square import Square


# To test if the Square constructor raises the TypeError exception, you use the assertRaises() method in a context manager like this:
class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square("10")


# 1. If you run the test again, it will fail:
# python -m unittest -v
# +++++++++++++++++++++++++++++++++
# test_area (test_square.TestSquare) ... ok
# test_length_with_wrong_type (test_square.TestSquare) ... FAIL
#
# ======================================================================
# FAIL: test_length_with_wrong_type (test_square.TestSquare)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "D:\python-unit-testing\test_square.py", line 13, in test_length_with_wrong_type
#     with self.assertRaises(TypeError):
# AssertionError: TypeError not raised
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# The test_length_with_wrong_type() method expected that the Square constructor raises a TypeError exception. However, it didn’t.


# 2. To make the test pass, you add another check to the Square() constructor: square-4
# python -m unittest -v
# +++++++++++++++++++++++++
# test_area (test.TestSquare.test_area) ... ok
# test_length_with_wrong_type (test.TestSquare.test_length_with_wrong_type) ... ok
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
