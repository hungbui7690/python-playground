import unittest


# Since the test_square.py needs to access the Square class, you have to import it from the square.py module:
from square import Square


# To create a test case, you define a new class called TestSquare that inherits from the TestCase class of the unittest module:
# To test the area() method, you add a method called test_area() to the TestSquare class like this:
class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


"""
In the test_area() method:

    First, create a new instance of the Square class and initialize its radius with the number 10.
    Second, call the area() method that returns the area of the square.
    Third, call the assertEqual() method to check if the result returned by the area() method is equal to an expected area (100).

If the area is equal to 100, the assertEqual() will pass the test. Otherwise, the assertEqual() will fail the test.
"""


# Before running the test, you need to call the main() function of the unittest module as follows:
if __name__ == "__main__":
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK


# The output indicates that one test has passed denoted by the dot (.) If a test failed, you would see the letter F instead of the dot (.)
