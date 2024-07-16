"""
Decimal constructor

- The Decimal constructor allows you to create a new Decimal object based on a value:

      Decimal(value='0', context=None)

- The value argument can be an integer, string, tuple, float, or another Decimal object. If you don’t provide the value argument, it defaults to '0'.

- If the value is a tuple, it should have three components: a sign (0 for positive or 1 for negative), a tuple of digits, and an integer exponent:

      (sign, (digit1,digit2, digit3,...), exponent)

- For example:

      3.14 = 314 x 10^-2

- The tuple has three elements as follows:

      sign is 0
      digits is (3,1,4)
      exponent is -2

"""

# Therefore, you’ll need to pass the following tuple to the Decimal constructor:
from decimal import Decimal
import decimal


x = Decimal((0, (3, 1, 4), -2))
print(x)  # 3.14


# Notice that the decimal context precision only affects the arithmetic operation, not the Decimal constructor. For example:
decimal.getcontext().prec = 2

pi = Decimal("3.14159")
radius = 1

print(pi)  # 3.14159

area = pi * radius * radius
print(area)  # 3.1


# When you use a float that doesn’t have an exact binary float representation, the Decimal constructor cannot create an accurate decimal representation. For example:
x = Decimal(0.1)
print(x)  # 0.1000000000000000055511151231257827021181583404541015625

# In practice, you’ll use a string or a tuple to construct a Decimal.


"""
Decimal arithmetic operations

- Some arithmetic operators don’t work the same as floats or integers, such as div (//) and mod (%).

- For decimal numbers, the // operator performs a truncated division:

      x // y = trunc( x / y)

- The Decimal class provides some mathematical operations such as sqrt and log. However, it doesn’t have all the functions defined in the math module.

- When you use functions from the math module for decimal numbers, Python will cast the Decimal objects to floats before carrying arithmetic operations. This results in losing the precision built in the decimal objects.

\\\\\\\\\\\\\\\\

Summary

  - Use the Python decimal module when you want to support fast correctly-rounded decimal floating-point arithmetic.
  - Use the Decimal class from the decimal module to create Decimal object from strings, integers, and tuples.
  - The Decimal numbers have a context that controls the precision and rounding mechanism.
  - The Decimal class doesn’t have all methods defined in the math module. However, you should use the Decimal’s arithmetic methods if they’re available.
"""
