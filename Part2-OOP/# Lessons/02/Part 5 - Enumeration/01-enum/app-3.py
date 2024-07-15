"""
Enumeration members are hashable

- Enumeration members are always hashable. It means that you can use the enumeration members as keys in a dictionary or as elements of a Set.


"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# The following example uses the members of the Color enumeration in a dictionary:
rgb = {Color.RED: "#ff0000", Color.GREEN: "#00ff00", Color.BLUE: "#0000ff"}
