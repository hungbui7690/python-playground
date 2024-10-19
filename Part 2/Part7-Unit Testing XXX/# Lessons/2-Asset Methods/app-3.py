"""
assertAlmostEqual

Introduction to the Python assertAlmostEqual() method

- The assertAlmostEqual() is a method of the TestCase class of the unittest module. The assertAlmostEqual() test if two values are approximately equal by doing the following:

    First, compute the difference.
    Second, round to the given number to decimal places (default 7)
    Third, compare the rounded value to zero.

- The following shows the syntax of the assertAlmostEqual() method:

    ~~ assertAlmostEqual(first, second, places=7, msg=None, delta=None)

- It uses the following check:

    round(first-second, 7) == 0

- The method uses places (or decimal places) to round the difference before comparing it to zero. Note that places are not significant digits.
- If you pass a delta instead of places then the difference between first and second must be less or equal to (or greater than) delta.
- The assertAlmostEqual() method allows you to use either places or delta. If you attempt to pass both arguments, you’ll get a TypeError.

\\\\\\\\\\\\\\\\\\\\\\\\\

- Since Python can only represent floats approximately, you need to use the assertAlmostEqual() method to test the result of the area() with another float.
- For example, the following test that uses the assertEqual() method will fail:

    self.assertEqual(0.1+0.1+0.1, 0.3)

- However, the following test that uses the assertAlmostEqual() method will pass:

    self.assertAlmostEqual(0.1+0.1+0.1, 0.3)

"""

import math


def area(radius: float) -> float:
    return math.pi * math.pow(radius, 2)
