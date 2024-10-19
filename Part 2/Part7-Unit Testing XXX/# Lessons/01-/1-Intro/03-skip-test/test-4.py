"""
Skipping a test class examples

- To skip a test class, you use the@unittest.skip() decorator at the class level.
- The following example uses the @unittest.skip() decorator at the class level. Hence, all tests of the TestDemo class are skipped:


"""

import unittest


@unittest.skip("Work in progress")
class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertIsNotNone([])


# test_case_1 (test_skipping.TestDemo) ... skipped 'Work in progress'
# test_case_2 (test_skipping.TestDemo) ... skipped 'Work in progress'
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK (skipped=2)
