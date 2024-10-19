"""
Python Decimal
- Many decimal numbers don’t have exact representations in binary floating-point such as 0.1. When using these numbers in arithmetic operations, you’ll get a result that you would not expect.

"""

from decimal import Decimal


x = 0.1
y = 0.1
z = 0.1
s = x + y + z
print(s)  # 0.30000000000000004


# To solve this problem, you use the Decimal class from the decimal module as follows:
x = Decimal("0.1")
y = Decimal("0.1")
z = Decimal("0.1")
s = x + y + z
print(s)  # 0.3


# The Python decimal module supports arithmetic that works the same as the arithmetic you learn at school.
# Unlike floats, Python represents decimal numbers exactly. And the exactness carries over into arithmetic. For example, the following expression returns exactly 0.0:
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))  # 0.0
