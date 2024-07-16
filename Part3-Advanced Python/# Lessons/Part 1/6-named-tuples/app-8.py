"""
Additional Python functions of named tuples

"""

from collections import namedtuple


Point2D = namedtuple("Point2D", "x y")


# Named tuples provide some useful functions out of the box. For example, you can use the equal operator (==) to compare two named tuple instances:
a = Point2D(100, 200)
b = Point2D(100, 200)


# If you use the class, you need to implement the __eq__ to get this function.
print(a == b)  # True


# Also, you can get the string representation of a named tuple:
# Again, if you use the class, you need to implement __rep__ method.
print(a)  # Point2D(x=100, y=200)


# Since a named tuple is a tuple, you can apply any function that is relevant to a regular tuple to a named tuple. For example:
print(max(a))  # 200
print(min(a))  # 100


# Summary
# Named tuples are tuples whose element positions have meaningful names.
# Use the namedtuple function of the collections standard library to create a named tuple class.
# Named tuples are immutable.
