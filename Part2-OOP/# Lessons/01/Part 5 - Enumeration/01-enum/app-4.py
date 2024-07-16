"""
Access an enumeration member by name and value

- The typical way to access an enumeration member is to use the dot notation (.) syntax as you have seen so far:

    Color.RED

- Because the Enum implements the __getitem__ method, you can also use a square brackets [] syntax to get a member by its name.

"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# For example, the following uses the square brackets [] syntax to get the RED member of the Color enumeration by its name:
print(Color["RED"])  # Color.RED


# Since an enumeration is callable, you can get a member by its value. For example, the following return the RED member of the Color enumeration by its value:
print(Color(1))  # Color.RED


# The following expression returns True because it accesses the same enumeration member using name and value:
print(Color["RED"] == Color(1))  # True
