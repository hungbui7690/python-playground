"""
AMAX
- The amax() function returns the maximum element of an array or maximum element along an axis. The following shows the syntax of the amax() function:

    numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)

- The amax() function is equivalent to the max() method of the ndarray object:

    ndarray.max(axis=None, out=None, keepdims=False, initial=<no value>, where=True)



"""

import numpy as np


# The following example uses the numpy amax() function to find the maximum value in a 1-D array:
a = np.array([1, 2, 3])
min = np.amax(a)
print(max)  # 3


# The following example uses the amax() function to find the maximum number in a 2-D array:
a = np.array([[1, 2], [3, 4]])
max = np.amax(a)
print(max)  # 4


# If you want to find the maximum value on each axis, you can use the axis argument. For example, the following uses the amax() function to find the maximum value on axis 0:
a = np.array([[1, 2], [3, 4]])
max = np.amax(a, axis=0)
print(max)  # [3 4]


# Similarly, you can use the amax() function to find the maximum value on axis 1:
a = np.array([[1, 2], [3, 4]])
max = np.amax(a, axis=1)
print(max)  # [2 4]
