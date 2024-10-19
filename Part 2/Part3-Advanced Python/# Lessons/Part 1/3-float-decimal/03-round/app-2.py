"""
How to round away from zero

- Python doesn’t provide a direct way to round a number away from zero as you might expect. For example:

    Number	  Rounding away from zero
    1.2	      1
    1.5	      2

- A common way to round a number away from zero is to use the following expression:

    int(x + 0.5)

"""

from math import copysign

# This expression works correctly for positive numbers. For example:

print(int(1.2 + 0.5))  # 1
print(int(1.5 + 0.5))  # 2


# However, it doesn’t work for the negative numbers:

print(int(-1.2 + 0.5))  # 0
print(int(-1.5 + 0.5))  # -1


# For negative numbers, you should subtract 0.5 instead of adding it.
# The following example works properly for the negative numbers:

print(int(-1.2 - 0.5))  # -1
print(int(-1.5 - 0.5))  # -2


# The following defines a helper function that rounds up a number:
def round_up(x):
    if x > 0:
        return int(x + 0.5)
    return int(x - 0.5)


# The Python math module provides you with a function called copysign():
#
#     math.copysign(x, y)
#
# The copysign() function returns the absolute value of x but the sign of y.
# And you can use this copysign() function to develop a round_up() function without checking whether x is positive or negative:


def round_upX(x):
    return int(x + copysign(0.5, x))


print(round_upX(1.3))
print(round_upX(-1.3))
