"""
ANY

"""

import numpy as np


# The following example uses the any() function to test if any elements of a multidimensional array evaluate to True:
a = np.array([[0, 1], [2, 3]])
result = np.any(a)
print(result)  # True


# Also, you can evaluate elements along an axis by passing the axis argument like this:
a = np.array([[0, 0], [0, 1]])
result = np.any(a, axis=0)
print(result)  # [False True]


# And axis-1:
a = np.array([[0, 0], [0, 1]])
result = np.any(a, axis=1)
print(result)  # [False True]
