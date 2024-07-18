"""
STACK
- The stack() function two or more arrays into a single array. Unlike the concatenate() function, the stack() function joins 1D arrays to be one 2D array and joins 2D arrays to be one 3D array.

- The following shows the syntax of the stack() function:

    numpy.stack((a1,a2,...),axis=0)

- In this syntax, the (a1, a2, …) is a sequence of arrays with ndarray type or array-like objects. All arrays a1, a2, .. must have the same shape.
- The axis parameter specifies the axis in the result array along which the function stacks the input arrays. By default, the axis is zero which joins the input arrays vertically.
- Besides the stack() function, NumPy also has vstack() function that joins two or more arrays vertically and hstack() function that joins two or more arrays horizontally.
"""

import numpy as np


# 1) Using stack() function to join 1D arrays
# The following example uses the stack() function to join two 1D arrays:
a = np.array([1, 2])
b = np.array([3, 4])

c = np.stack((a, b))
print(c)
# [[1 2]
#  [3 4]]
