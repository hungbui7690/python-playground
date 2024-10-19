"""
Running tests without calling unittest.main() function


"""

import unittest
from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


# 1. remove the if block that calls the unittest.main() function:


# 2. execute the following command to run the test:
# This command discovers all the test classes whose names start with Test* located in the test_* file and execute the test methods that start with test*. the -m option stands for the module.
# python -m unittest
# .
#
# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s
#
# OK


# 3. To display more information, you can add -v option to the above command. -v stands for verbosity. It’s like calling the unittest.main() with verbosity argument with value 2.
# python -m unittest -v
# test_area (test_square.TestSquare.test_area) ... ok
#
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
