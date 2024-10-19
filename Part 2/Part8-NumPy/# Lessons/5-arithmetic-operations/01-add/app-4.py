"""
ADD

- The + or add() function of two equal-sized arrays perform element-wise additions. It returns the sum of two arrays, element-wise.

"""

import numpy as np


# Likewise, you can use the add() function to add two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.add(a, b)
print(c)
# [[ 6  8]
#  [10 12]]


# Summary
# Use the + operator or add() function to add two equal-sized array.
