"""
Equality testing
- The following shows the isclose() function signature:

    isclose(a, b, rel_tol=1e-9, abs_tol=0.0)

"""

from math import isclose


# Let’s take a look at the following example:
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)  # False


# Internally, Python cannot use a finite number of digits to represent the numbers x and y:
print(format(x, ".20f"))  # 0.30000000000000004441
print(format(y, ".20f"))  # 0.29999999999999998890
# Note that the number of digits is infinite. We just show the first 20 digits.


# One way to work around this problem is to round both sides of the equality expression to a number of significant digits. For example:
x = 0.1 + 0.1 + 0.1
y = 0.3
print(round(x, 3) == round(y, 3))  # True


# This workaround doesn’t work in all cases.
# PEP485 provides a solution that fixes this problem by using relative and absolute tolerances.
# It provides the isclose() function from the math module returns True if two numbers are relatively close to each other.
x = 0.1 + 0.1 + 0.1
y = 0.3

print(isclose(x, y))  # True


# Summary
# Python uses float class to represent real numbers.
# Python uses a fixed number of bytes (8 bytes) to represent floats. Therefore, it can represent some numbers in binary approximately.
# Use the isclose() function from the math module to test equality for floating-point numbers
