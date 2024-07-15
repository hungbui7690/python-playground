"""
Enum aliases & @enum.unique Decorator
- By definition, the enumeration member values are unique. However, you can create different member names with the same values.

"""

# For example, the following defines the Color enumeration:
from enum import Enum
from pprint import pprint


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3


"""
In this example, the Color enumeration has the RED, CRIMSON, and SALMON members with the same value 1.

When you define multiple members in an enumeration with the same values, Python does not create different members but aliases.

In this example, the RED is the main member while the CRIMSON and SALMON members are the aliases of the RED member
"""

# The following statements return True because CRIMSON and SALMON members are RED member:
print(Color.RED is Color.CRIMSON)  # True
print(Color.RED is Color.SALMON)  # True


# When you look up a member by value, you’ll always get the main member, not aliases. For example, the following statement returns the RED member:
print(Color(1))  # Color.RED


# When you iterate the members of an enumeration with aliases, you’ll get only the main members, not the aliases. For example:
for color in Color:
    print(color)

# It returns only 3 members
# Color.RED
# Color.GREEN
# Color.BLUE


# To get all the members including aliases, you need to use the __member__ property of the enumeration class. For example:
pprint(Color.__members__)
"""
mappingproxy({'BLUE': <Color.BLUE: 3>,
            'CRIMSON': <Color.RED: 1>,
            'GREEN': <Color.GREEN: 2>,
            'RED': <Color.RED: 1>,
            'SALMON': <Color.RED: 1>})

- As shown clearly from the output, the CRIMSON and SALMON reference the same object which is referenced by the RED member: <Color.RED: 1>
"""
