"""
Unit Test

"""


# To make the test pass, you add another check to the Square() constructor:


class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError("Length must be an integer or float")

        self.length = length

    def area(self):
        return self.length * self.length
