"""
Enumerations are immutable

- Enumerations are immutable. It means you cannot add or remove members once an enumeration is defined. And you also cannot change the member values.

"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# The following example attempts to assign a new member to the Color enumeration and causes a TypeError:
# TypeError: 'EnumMeta' object does not support item assignment
Color["YELLOW"] = 4


# The following example attempts the change the value of the RED member of the Color enumeration and causes an AttributeError:
# AttributeError: can't set attribute
Color.RED.value = 100
