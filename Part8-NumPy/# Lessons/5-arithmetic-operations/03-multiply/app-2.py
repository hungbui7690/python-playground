"""
MULTIPLY

- The * operator or multiply() function returns the product of two equal-sized arrays by performing element-wise multiplication.

"""

import numpy as np


# The following example uses the * operator to get the products of two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a * b
print(c)
# [[ 5 12]
#  [21 32]]


c = np.multiply(a, b)
print(c)
# [[ 5 12]
#  [21 32]]


# Summary
# Use the * operator or multiply() function to find the product of two equal-sized arrays.
