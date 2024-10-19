"""
Instantiating named tuples

"""

from collections import namedtuple


Point2D = namedtuple("Point2D", ["x", "y"])


# The Point2D is a class, which is a subclass of the tuple. And you can create new instances of the Point2D class like you do with a regular class. For example:
point = Point2D(100, 200)

# Or you can use the keyword arguments:
pointX = Point2D(x=100, y=200)


# The point object is an instance of the Point2D class. Therefore, it’s an instance of the tuple class:
print(isinstance(point, Point2D))  # True
print(isinstance(point, tuple))  # True
