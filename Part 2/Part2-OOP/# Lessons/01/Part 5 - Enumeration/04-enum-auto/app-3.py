"""
How enum() auto works

- Technically, the auto() calls the _generate_next_value_() method to generate values for the members. Here’s the syntax of the _generate_next_value_() method:

    _generate_next_value_(name, start, count, last_values)

- The _generate_next_value_() has the following parameters:

    name is the member’s name
    start is the starting value of the enum members.
    count is the number of enum members, including aliases, that have been created.
    last_values is a list of all preceding values used for the enum members.

- By default, the _generate_next_value_() generates the next number in a sequence of integers starting from one. However, Python may change this logic in the future.

- It’s possible to override the _generate_next_value_() method to add a custom logic that generates unique values. If so, you need to place the _generate_next_value_() method before defining all the members.


"""

# The following shows how to override the _generate_next_value_() method to generate values for members by using their names:
from enum import Enum, auto


class State(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()


for state in State:
    print(state.name, state.value)
# PENDING   pending
# FULFILLED fulfilled
# REJECTED  rejected

# Summary
# Use enum auto() class to generate unique values for enumeration members.
