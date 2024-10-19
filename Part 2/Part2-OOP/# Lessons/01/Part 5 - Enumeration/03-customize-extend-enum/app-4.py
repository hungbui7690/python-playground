"""
Implementing the __bool__ method


"""

from enum import Enum
from functools import total_ordering


@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f"{self.name.lower()}({self.value})"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, PaymentStatus):
            return self is other

        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, PaymentStatus):
            return self.value < other.value

        return False

    # 2. To customize this behavior, you need to implement the __bool__ method. Suppose you want the COMPLETED and REFUNDED members to be True while the PENDING to be False.
    def __bool__(self):
        if self is self.COMPLETED:
            return True

        return False


# 1. By default, all members of an enumeration are truthy. For example:
for member in PaymentStatus:
    print(member, bool(member))

"""
- Without __bool__

    pending(1)    True
    completed(2)  True
    refunded(3)   True

- With __bool__

    pending(1)    False
    completed(2)  True
    refunded(3)   False

"""
