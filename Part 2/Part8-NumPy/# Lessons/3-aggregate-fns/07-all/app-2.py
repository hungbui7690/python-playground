"""
ALL


"""

import numpy as np


# The following example uses the all() function to test if all elements of a multidimensional array evaluate to True:
a = np.array([[0, 1], [2, 3]])
result = np.all(a)

print(result)  # False


# Also, you can evaluate elements along an axis by passing the axis argument like this:
a = np.array([[0, 1], [2, 3]])
result = np.all(a, axis=0)
print(result)  # [False True]


# Axis-1
a = np.array([[0, 1], [2, 3]])
result = np.all(a, axis=1)
print(result)  # [False True]
