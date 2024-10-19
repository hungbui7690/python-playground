"""
Skipping a test with a condition

- Sometimes, you want to skip a test conditionally. For example, you may want to skip a test if the current platform, where the test is running, is windows.

- To do that you use the @unittest.skipIf() decorator:

    @unittest.skipIf(condition, reason)

- This will skip the test if the condition is true. Also, it’ll display the reason for skipping the test in the test result.

"""

import unittest

from sys import platform


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    @unittest.skipIf(platform.startswith("win"), "Do not run on Windows")
    def test_case_2(self):
        self.assertIsNotNone([])


# test_case_1 (test.TestDemo.test_case_1) ... ok
# test_case_2 (test.TestDemo.test_case_2) ... skipped 'Do not run on Windows'
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK (skipped=1)


# In this example, we skip the test_case_2() method if the current platform is windows. To get the current platform where the test is running, we use the sys.platform property.


# Unlike the @unittest.skipIf decorator, the @unittest.skipUnless skips a test uncles a condition is true:
# @unittest.skipUnless(condition, reason)


# Summary
# Use the @unittest.skip() decorator, skipTest() method, or raise SkipTest exception to skip a test.
# Use the @unittest.skipIf() or @unittest.skipUnless() to skip a test conditionally.
