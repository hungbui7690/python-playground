import unittest
from app import area
from math import pi


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0.1), pi * 0.1 * 0.1)


# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK


# The assertNotAlmostEqual() method is the opposite of the assertAlmostEqual() method. It tests if two values are not approximately equal.
