"""
Membership and equality
- To check if a member is in an enumeration, you use the in operator


"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# To check if a member is in an enumeration, you use the in operator. For example:
if Color.RED in Color:
    print("Yes")
# Yes


# To compare two members, you can use either is or == operator. For example:
if Color.RED is Color.BLUE:
    print("red is blue")
else:
    print("red is not blue")
# red is not blue


# Note that a member and its associated value are not equal. The following example returns False:
if Color.RED == 1:
    print("Color.RED == 1")
else:
    print("Color.RED != 1")
# Color.RED != 1
