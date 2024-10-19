"""
TEST FIXTURES

Class-level fixtures

- The setUpClass() and tearDownClass() are class-level fixtures:

    The setUpClass() runs before all test methods of a class
    The tearDownClass() runs after all test methods of a class.

"""

import unittest


def setUpModule():
    print("Running setUpModule")


def tearDownModule():
    print("Running tearDownModule")


class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")

    def test_case_1(self):
        self.assertEqual(5 + 5, 10)

    def test_case_2(self):
        self.assertEqual(1 + 1, 2)


# Running setUpModule
# Running setUpClass
# test_case_1 (test_my_module.TestMyModule.test_case_1) ... ok
# test_case_2 (test_my_module.TestMyModule.test_case_2) ... ok
# Running tearDownClass
# Running tearDownModule
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
