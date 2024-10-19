"""
TEST FIXTURES

Introduction to the Python Test fixtures

- By definition, a test fixture is a function or method that runs before and after a block of test code executes. In other words, it is a step carried out before or after a test.
Module-level fixtures

- Suppose you have a test module called test_my_module.py. In the test_my_module.py, the setUpModule() and tearDownModule() functions are the module-level fixtures.

    The setUpModule() function runs before all test methods in the test module.
    The tearDownModule() function runs after all methods in the test module.

"""

import unittest


def setUpModule():
    print("Running setUpModule: this runs before all test methods")


def tearDownModule():
    print("Running tearDownModule: this runs after all test methods")


class TestMyModule(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(5 + 5, 10)

    def test_case_2(self):
        self.assertEqual(1 + 1, 2)


# Running setUpModule
# test_case_1 (test_my_module.TestMyModule.test_case_1) ... ok
# test_case_2 (test_my_module.TestMyModule.test_case_2) ... ok
# Running tearDownModule
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s
#
# OK


# In this example, the setUpModule() function runs before all the test methods and the tearDownModule() function runs after all the test methods.
