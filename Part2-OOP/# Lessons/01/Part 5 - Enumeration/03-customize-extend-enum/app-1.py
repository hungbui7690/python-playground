"""
Customize and Extend Python Enum Class

- Python enumerations are classes. It means that you can add methods to them, or implement the dunder methods to customize their behaviors.


"""

# The following example defines the PaymentStatus enumeration class:

from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3


# The PaymentStatus enumeration has three members: PENDING, COMPLETED, and REFUND.
# The following displays the member of the PaymentStatus‘ member:
print(PaymentStatus.PENDING)  # PaymentStatus.PENDING
