"""
@enum.unique decorator

- To define an enumeration with no aliases, you can carefully use unique values for the members.

"""

# To ensure an enumeration has no alias, you can use the @enum.unique decorator from the enum module.
# When you decorate an enumeration with the @enum.unique decorator, Python will throw an exception if the enumeration has aliases.
# For example, the following will raise a ValueError:
import enum
from enum import Enum


@enum.unique
class Day(Enum):
    MON = "Monday"
    TUE = "Monday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


# ValueError: duplicate values found in <enum 'Day'>: TUE -> MON


# Summary
# When an enumeration has different members with the same values, the first member is the main member while others are aliases of the main member.
# Use the @enum.unique decorator from the enum module to enforce the uniqueness of the values of the members.
