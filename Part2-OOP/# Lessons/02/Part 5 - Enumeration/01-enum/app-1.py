"""
Enumeration
- By definition, an enumeration is a set of members that have associated unique constant values. Enumeration is often called enum.

- Python provides you with the enum module that contains the Enum type for defining new enumerations. And you define a new enumeration type by subclassing the Enum class.


"""

# First, import the Enum type from the enum module:
from enum import Enum


# Second, define the Color class that inherits from the Enum type:
class Color(Enum):
    # Third, define the members of the Color enumeration:
    RED = 1
    GREEN = 2
    BLUE = 3


# Note that the enumeration’s members are constants. Therefore, their names are in uppercase letters by convention.
# In this example, the Color is an enumeration. The RED, GREEN, and BLUE are members of the Color enumeration. They have associated values 1, 2, and 3.
# The type of a member is the enumeration to which it belongs.


# The following illustrates that the type of Color.RED is the Color enumeration:
print(type(Color.RED))  # <enum 'Color'>


# The Color.RED is also an instance of the Color enumeration:
print(isinstance(Color.RED, Color))  # True


# And it has the name and value attributes:
print(Color.RED.name)  # RED
print(Color.RED.value)  # 1
