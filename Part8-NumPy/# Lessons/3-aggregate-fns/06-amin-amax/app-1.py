"""
AMIN
- The amin() function returns the minimum element of an array or minimum element along an axis. Here’s the syntax of the amin() function:

    numpy.amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where= <no value>)

- The amin() function is equivalent to the min() method of the ndarray object:

    ndarray.min(axis=None, out=None, keepdims=False, initial=<no value>, where=True)

"""

import numpy as np


# 1) Using numpy amin() function on 1-D array
a = np.array([1, 2, 3])
min = np.amin(a)
print(min)  # 1


# 2) Using numpy amin() function on 2D array
a = np.array([[1, 2], [3, 4]])
min = np.amin(a)
print(min)  # 1


# If you want to find the minimum value on each axis, you can use the axis argument. For example, the following uses the amin() function to find the minimum value on axis 0:
a = np.array([[1, 2], [3, 4]])
min = np.amin(a, axis=0)
print(min)  # [1 2]


# Similarly, you can use the amin() function to find the minimum value on axis 1:
a = np.array([[1, 2], [3, 4]])
min = np.amin(a, axis=1)
print(min)  # [1 3]
