"""
Python Operator Overloading

"""


# Python has a better way to implement add(). Instead of using the add() method, you can use the built-in operator (+) like this:
# c = a + b


# When you use the + operator on the Point2D object, Python will call the special method __add__() on the object. The following calls are equivalent:
# c = a + b
# c = a.__add__(b)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, point):
        if not isinstance(point, Point2D):
            raise ValueError("The other must be an instance of the Point2D")

        return Point2D(self.x + point.x, self.y + point.y)


if __name__ == "__main__":
    a = Point2D(10, 20)
    b = Point2D(15, 25)
    c = a + b
    print(c)  # (25,45)
