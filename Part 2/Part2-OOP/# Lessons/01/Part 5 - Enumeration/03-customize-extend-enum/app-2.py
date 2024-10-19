"""
Customize and Extend Python Enum Class

- Python enumerations are classes. It means that you can add methods to them, or implement the dunder methods to customize their behaviors.


"""

from enum import Enum


class PaymentStatus(Enum):
    # (1)
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    # (2) To customize how the PaymentStatus member’s is represented in the string, you can implement the __str__ method. For example:
    def __str__(self):
        return f"{self.name.lower()}({self.value})"

    # (5)
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, PaymentStatus):
            return self is other

        return False


print(PaymentStatus.PENDING)  # (3) pending(1)


# (4) Implementing __eq__ method
# The following attempts to compare a member of the PaymentStatus enum class with an integer:
# Without __eq__, it shows nothing because the PaymentStatus.PENDING is not equal to integer 1.
if PaymentStatus.PENDING == 1:
    print("The payment is pending.")
# The payment is pending.


""" 
In the __eq__ method:

    If the value to compare is an integer, it compares the value of the member with the integer.
    If the value to compare is an instance of the PaymentStatus enumeration, it compares the value with the member of the PaymentStatus member using the is operator.
    Otherwise, it returns False.
"""
