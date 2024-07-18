"""
TEST FIXTURES

Method-level fixtures

- The setUp() and tearDown() are method-level fixtures:

    The setUp() runs before every test method in the test class.
    The tearDown() runs after every test method in the test class.

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

    def setUp(self):
        print("")
        print("Running setUp")

    def tearDown(self):
        print("Running tearDown")

    def test_case_1(self):
        print("Running test_case_1")
        self.assertEqual(5 + 5, 10)

    def test_case_2(self):
        print("Running test_case_2")
        self.assertEqual(1 + 1, 2)


# Running setUpModule
# Running setUpClass
# test_case_1 (test_my_module.TestMyModule.test_case_1) ...
# Running setUp
# Running test_case_1
# Running tearDown
# ok
# test_case_2 (test_my_module.TestMyModule.test_case_2) ...
# Running setUp
# Running test_case_2
# Running tearDown
# ok
# Running tearDownClass
# Running tearDownModule
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.003s
#
# OK


# In this example, the setUp() and tearDown() executes before and after each test method including test_case_1() and test_case_2().
