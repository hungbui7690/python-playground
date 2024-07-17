"""
Accessing data of a named tuple

- A named tuple is a regular tuple. Therefore, you can apply all tuple operations on a named tuple.
- To access data in a named tuple, you can use:

    Slicing
    Unpacking
    Indexing
    and iterating

"""

from collections import namedtuple


Point2D = namedtuple("Point2D", ["x", "y"])


point = Point2D(100, 200)


# unpacking
x, y = point
print(f"({x}, {y})")  # (100, 200)

# indexing
x = point[0]
y = point[1]
print(f"({x}, {y})")  # (100, 200)

# iterating

for coordinate in point:
    print(coordinate)
