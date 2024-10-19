"""
Python Operator Overloading

"""


# Suppose you have a 2D point class with x and y coordinate attributes:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


# To add two Point2D objects, you can define an add() method as follows:
class Point2Dx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def add(self, point):
        if not isinstance(point, Point2Dx):
            raise ValueError("The other must be an instance of the Point2D")

        return Point2Dx(self.x + point.x, self.y + point.y)


# The add() method raises an error if the point is not an instance of the Point2D class. Otherwise, it returns a new Point2D object whose x and y coordinates are the sums of x and y coordinates of two points.


# The following creates two instances of the Point2D class and use the add() method to add two points:
a = Point2Dx(10, 20)
b = Point2Dx(15, 25)
c = a.add(b)
print(c)  # (25,45)


# This code works perfectly fine. But Python has a better way to implement it. Instead of using the add() method, you can use the built-in operator (+) like this:
# c = a + b
