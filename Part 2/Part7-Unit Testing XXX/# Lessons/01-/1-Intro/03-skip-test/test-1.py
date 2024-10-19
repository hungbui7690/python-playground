"""
SKIPPING TESTS

- The unittest module allows you to skip a test method or a test class. To skip a test, you have three available options:

    Use the @unittest.skip() decorator.
    Call the skipTest() method of the TestCase class.
    Raise the SkipTest exception.

- The following example uses the @unittest.skip() decorator to skip the test_case_2() method unconditionally:

"""

import unittest


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skip("Work in progress")
    def test_case_2(self):
        pass


# test_case_1 (test.TestDemo.test_case_1) ... ok
# test_case_2 (test.TestDemo.test_case_2) ... skipped 'Work in progress'
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK (skipped=1)


# The output shows that two tests were executed and one was skipped. For the skipped test, the output shows the message that we passed to the @unittest.skip() decorator.
