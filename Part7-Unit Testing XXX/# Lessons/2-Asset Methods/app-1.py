"""
assertEqual

Introduction to the Python assertEqual() method
- The assertEqual() is a method of the TestCase class of the unittest module. The assertEqual() tests if two values are equal:

   assertEqual(first, second, msg=None)

- If the first value does not equal the second value, the test will fail.
- The msg is optional. If the msg is provided, it’ll be shown on the test result if the test fails.

"""


# 1. create a new module called app.py and define the add() function:
def add(a, b):
    return a + b
