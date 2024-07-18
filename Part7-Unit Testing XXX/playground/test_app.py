# The assertIsNot() tests if the first object is not the same as the second one:
# assertIsNot(first, second, msg=None)


import unittest


class TestInteger(unittest.TestCase):
    def test_integer_different_value(self):
        x = 10
        y = 20
        self.assertIsNot(x, y)

    def test_integer_same_value(self):
        x = 10
        y = 10
        self.assertIs(x, y)


# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK


# In this example, we use the assertIsNot() method to test if two integer variables reference different objects. Since their values are different, they reference different objects.
# In the second test case, we use the assertIs() method to test if two integer variables reference the same object. Because their values are the same, they reference the same object.


# Summary
# Use the assertIs() method to test if two objects are the same.
# Use the assertIsNot() method to test if two variables reference different objects.
