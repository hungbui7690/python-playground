"""
The floor division in Python

- To understand the floor division, you first need to understand the floor of a real number.

- The floor of a real number is the largest integer less than or equal to the number. In other words:

    floor(r) = n, n is an integer and n <= r


"""

from math import floor


# For example, the floor of 3.4 is 3 because 3 is the largest integer less than or equal to 3.4. The floor of 3.9 is also 3. And the floor of 3 is 3 obviously:
print(floor(3.4))
print(floor(3.9))
print(floor(3))
# Notice that the floor division of a number is not always the same as truncation. The floor division is the same as truncation only when the numbers are positive.


# The floor() function of the math module returns the floor division of two integers. For example:
a = 10
b = 3
print(a // b)  # 3
print(floor(a / b))  # 3


# As you can see clearly from the output, the floor() function returns the same result as the floor division operator (//). It’s also true for the negative numbers:
a = 10
b = -3
print(a // b)  # -4
print(floor(a / b))  # -4


# Summary
# Python uses // as the floor division operator and % as the modulo operator.
# If the numerator is N and the denominator D, then this equation N = D * ( N // D) + (N % D) is always satisfied.
# Use floor division operator // or the floor() function of the math module to get the floor division of two integers.
