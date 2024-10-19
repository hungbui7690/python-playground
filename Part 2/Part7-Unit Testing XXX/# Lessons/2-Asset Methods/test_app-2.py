# If the first is equal to the second, the test will fail. Otherwise, it’ll pass. For example:


import unittest
from main import add


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        self.assertNotEqual(add(0.2, 0.1), 0.3)


# test_add (test_main.TestMain) ... ok
# test_add_floats (test_main.TestMain) ... ok
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK


# Since 0.2 + 0.1 returns 0.30000000000000004, it’s not equal to 0.3. Therefore, the following test passes:
# self.assertNotEqual(add(0.2, 0.1), 0.3)


# Summary
# Use the assertEqual() method to test if two values are equal.
# Use the assertNotEqual() method to test if two values are not equal.
