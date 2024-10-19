"""
Iterate enumeration members

"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Enumerations are iterables so you can iterate them using a for loop. For example:
for color in Color:
    print(color)

"""
Color.RED
Color.GREEN
Color.BLUE
"""


# Notice that the order of the members is the same as in the enumeration definition.
# Also, you can use the list() function to return a list of members from an enumeration:
print(list(Color))
# [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
