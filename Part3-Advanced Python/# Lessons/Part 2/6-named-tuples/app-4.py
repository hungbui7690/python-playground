"""
Creating named tuple classes

- To create a named tuple class, you need to the namedtuple function of the collections standard library.

- The namedtuple is a function that returns a new named tuple class. In other words, the namedtuple() is a class factory.

"""

# To use the namedtuple function, you need to import it from the collections module first:
from collections import namedtuple


"""
The namedtuple function accepts the following arguments to generate a class:

  A class name that specifies the name of the named tuple class.
  A sequence of field names that correspond to the elements of tuples. The field names must be valid variable names except that they cannot start with an underscore (_).
"""


# For example, the following uses the namedtuple function to create the Point2D class:
Point2D = namedtuple("Point2D", ["x", "y"])


# The namedtuple also can accept fields names as:
# 1) A tuple of string:

Point2DX = namedtuple("Point2D", ("x", "y"))


# 2) Or a single string with field names separated by commas:
Point2DY = namedtuple("Point2D", ("x, y"))


# 3) Or a single string with field names separated by whitespaces
Point2DZ = namedtuple("Point2D", "x y")
