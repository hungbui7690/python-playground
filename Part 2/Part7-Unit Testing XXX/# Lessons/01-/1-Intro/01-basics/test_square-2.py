import unittest
from square import Square


# To get more detailed information on the test result, you pass the verbosity argument with the value 2 to the unittest.main() function:


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


# 0 (quiet): you just get the total numbers of tests executed and the global result
# 1 (default): you get the same plus a dot for every successful test or a F for every failure
# 2 (verbose): you get the help string of every test and the result
if __name__ == "__main__":
    # get more detail info
    unittest.main(verbosity=2)


# test_area (__main__.TestSquare.test_area) ... ok
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK


# The output list the test case with the result ok this time instead of the dot (.)
