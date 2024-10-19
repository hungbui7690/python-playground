"""
MULTIPLY

- The * operator or multiply() function returns the product of two equal-sized arrays by performing element-wise multiplication.

"""

import numpy as np


# The following example uses the * operator to get the products of two 1-D arrays:
a = np.array([1, 2])
b = np.array([3, 4])
c = a * b
print(c)  # [3 8]


c = np.multiply(a, b)
print(c)  # [3 8]
