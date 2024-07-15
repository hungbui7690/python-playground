"""
Inherits from an enumeration

- An enumeration cannot be inherited unless it contains no members.

"""

from enum import Enum


class Color(Enum):
    pass


class RGB(Color):
    RED = 1
    GREEN = 2
    BLUE = 3


# However, the following example won’t work because the RGB enumeration has members:
# TypeError: <enum 'RGBA'> cannot extend <enum 'RGB'>
class RGBA(RGB):
    ALPHA = 4
