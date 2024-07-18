"""
What is a unit test

- A unit test is an automated test that:

    + Verifies a small piece of code called a unit. A unit can be a function or a method of a class.
    + Runs very fast.
    + Executes in an isolated manner.

- The idea of unit testing is to check each small piece of your program to ensure it works properly. It’s different from integration testing which tests that different parts of the program work well together.

- The goal of a unit test is to find bugs. Also, a unit test can help refactor existing code to make it more testable and robust.

- Python provides you with a built-in module unittest that allows you to carry out unit testing effectively.

\\\\\\\\\\\\\\\\\\

xUnit terminology

- The unittest module follows the xUnit philosophy. It has the following major components:

    + System under test is a function, a class, a method that will be tested.
    + Test case class (unittest.TestCase): is the base class for all the test classes. In other words, all test classes are subclasses of the TestCase class in the unittest module.
    + Test fixtures are methods that execute before and after a test method executes.
    + Assertions are methods that check the behavior of the component being tested.
    + Test suite is a group of related tests executed together.
    + Test runner is a program that runs the test suite.

"""

# Suppose you have Square class that has a property called length and a method area() that returns the area of the square. The Square class is in the square.py module:


class Square:
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length * self.length
