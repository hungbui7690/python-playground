"""
VSTACK


"""

import numpy as np


# 2) Using vstack() function to join elements of 2D arrays
# The following example uses the vstack() function to join elements of two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.vstack((a, b))
print(c)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# Summary
# Use the numpy vstack() function to join two or more arrays vertically.
