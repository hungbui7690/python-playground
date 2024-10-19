"""
Extend Python enum classes

- Python doesn’t allow you to extend an enum class unless it has no member.
- However, this is not a limitation.
- Because you can define a base class that has methods but no member and then extend this base class.


"""

# First, define the OrderedEnum base class that orders the members by their values:
from enum import Enum
from functools import total_ordering


@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented


# Second, define the ApprovalStatus that extends the OrderedEnum class:
class ApprovalStatus(OrderedEnum):
    PENDING = 1
    IN_PROGRESS = 2
    APPROVED = 3


# Third, compare the members of the ApprovalStatus enum class:
status = ApprovalStatus(2)
if status < ApprovalStatus.APPROVED:
    print("The request has not been approved.")
# The request has not been approved.


# Summary
# Implement dunder methods to customize the behavior of Python enum classes.
# Define an enum class with no members and methods and extends this base class.
