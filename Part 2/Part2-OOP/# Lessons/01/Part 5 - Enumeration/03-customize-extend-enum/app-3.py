"""
Implementing __lt__ method

- less than
- Suppose that you want the members of the PaymentStatus to follow have a sort order based on their value. And you also want to compare them with an integer.


"""

from enum import Enum
from functools import total_ordering  # 1.


# 2.
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

    # 3.
    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, PaymentStatus):
            return self.value < other.value

        return False


# compare with an integer
status = 1
if status < PaymentStatus.COMPLETED:
    print("The payment has not completed")

# compare with another member
status = PaymentStatus.PENDING
if status >= PaymentStatus.COMPLETED:
    print("The payment is not pending")
