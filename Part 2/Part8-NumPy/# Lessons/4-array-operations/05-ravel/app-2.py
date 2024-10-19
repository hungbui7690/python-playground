"""
RAVEL

2) ravel() function vs. flatten() method

"""

import numpy as np


# The flatten() method creates a copy of an input array while the ravel() function creates a view of the array. The ravel() only makes a copy of an array if needed. For example:
a = np.array([[1, 2], [3, 4]])
b = np.ravel(a)

b[0] = 0

print(b)  # [0 2 3 4]
print(a)
# [[0 2]
#  [3 4]]


# Another important difference between the flatten() method and ravel() function is that you can call the flatten() method on a ndarray while you can call the ravel() function on an array-like object.


# Summary
# Use the numpy ravel() function to return a contiguous flattened array.
