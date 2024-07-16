"""
enum auto


"""

# To make it more convenient, Python 3.6 introduced the auto() helper class in the enum module, which automatically generates unique values for the enumeration members. For example:

# First, import the Enum and auto classes from the enum module.
from enum import Enum, auto


class State(Enum):
    # Second, call the auto() to generate a unique value for each member of the State enumeration.
    # By default, the auto() class generates a sequence of integer numbers starting from 1.
    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

    def __str__(self):
        return f"{self.name(self.value)}"


# The following shows the values of the State enumeration’s members:
for state in State:
    print(state.name, state.value)

# PENDING 1
# FULFILLED 2
# REJECTED 3
