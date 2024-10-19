"""
SKIPPING TESTS
- Also, you can raise the SkipTest exception in a test method to skip it.


"""

import unittest


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        raise unittest.SkipTest("Work in progress")


# test_case_1 (test.TestDemo.test_case_1) ... ok
# test_case_2 (test.TestDemo.test_case_2) ... skipped 'Work in progress'
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK (skipped=1)
