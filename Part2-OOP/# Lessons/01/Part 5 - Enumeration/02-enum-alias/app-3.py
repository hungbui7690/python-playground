"""
@enum.unique decorator

- To define an enumeration with no aliases, you can carefully use unique values for the members.

"""

# To define an enumeration with no aliases, you can carefully use unique values for the members. For example:
from enum import Enum


class Day(Enum):
    # But you can accidentally use the same values for two members like this:
    MON = "Monday"
    TUE = "Monday"

    # TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


# In this example, the TUE member is the alias of the MON member, which you may not expect.
