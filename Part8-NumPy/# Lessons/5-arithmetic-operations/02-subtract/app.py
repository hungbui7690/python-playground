"""
SUBTRACT

- The - or subtract() function returns the difference between two equal-sized arrays by performing element-wise subtractions.

"""

import numpy as np


# The following example uses the - operator to find the difference between two 1-D arrays:
a = np.array([1, 2])
b = np.array([3, 4])
c = b - a
print(c)  # [2 2]
# [2-1, 3-2] = [1,1]


# Similarly, you can use the subtract() function to find the difference between two 1D arrays like this:
a = np.array([1, 2])
b = np.array([3, 4])
c = np.subtract(b, a)
print(c)  # [2 2]


# The following example uses the - operator to find the difference between two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = b - a
print(c)
# [[4 4]
#  [4 4]]


# Likewise, you can use the subtract() function to find the difference between two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.subtract(b, a)
print(c)
# [[4 4]
#  [4 4]]


# Summary
# Use the subtract operator (-) or subtract() function to find the difference between two equal-sized arrays.
