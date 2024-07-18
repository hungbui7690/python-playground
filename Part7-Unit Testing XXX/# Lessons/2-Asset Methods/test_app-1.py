# 2. create a test module test_app.py to test the add() function:

import unittest
from app import add


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


# 3. python -m unittest test_app.py -v
#
# +++++++++++++++++++++
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
