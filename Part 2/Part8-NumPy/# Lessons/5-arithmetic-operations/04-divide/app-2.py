"""
DIVIDE

- The / operator or divide() function returns the quotient of two equal-sized arrays by performing element-wise division.

"""

import numpy as np


# The following example uses the / operator to find the quotient of two 2D arrays:
a = np.array([[10, 8], [6, 4]])
b = np.array([[5, 2], [2, 1]])
c = a / b
print(c)
# [[2. 4.]
#  [3. 4.]]


# Likewise, you can use the divide() function to find the products of two 2D arrays:
c = np.divide(a, b)
print(c)
# [[2. 4.]
#  [3. 4.]]


# Summary
# Use the * operator or divide() function to find the quotient of two equal-sized arrays.
