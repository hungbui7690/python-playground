"""
NamedTuple

"""


# To compare if two points are the same, you need to implement the __eq__ method:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # The __eq__ method checks if a point is an instance of the Point2D class and returns True if both x-coordinate and y-coordinate are equal.
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False


a = Point2D(100, 200)
b = Point2D(100, 200)


# The following shows how to compare two instances of the Point2D class:
print(a is b)  # False
print(a == b)  # true


"""
The Point2D might work as you expected. However, you need to write a lot of code.

To combine the simplicity of a tuple and the obvious of a class, you can use a named tuple:

  TUPLE + CLASS = NAMED TUPLE

Named tuples allow you to create tuples and assign meaningful names to the positions of the tuple’s elements.

Technically, a named tuple is a subclass of tuple. On top of that, it adds property names to the positional elements.

"""
