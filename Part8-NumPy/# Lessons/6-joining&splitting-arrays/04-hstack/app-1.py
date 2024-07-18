"""
HSTACK
- The hstack() function joins elements of two or more arrays into a single array horizontally (column-wise).

- The following shows the syntax of the hstack() function:

    numpy.hstack((a1,a2,...))

- In this syntax, the (a1, a2, …) is a sequence of arrays with the ndarray type.
- All arrays a1, a2, .. must have the same shape along all but the second axis. If all arrays are 1D arrays, then they can have any length.
- If you want to join two or more arrays vertically, you can use the vstack() function.


"""

import numpy as np


# 1) Using numpy hstack() function to join elements of 1D arrays
# The following example uses the hstack() function to join two 1D arrays horizontally:
a = np.array([1, 2])
b = np.array([3, 4, 5])

c = np.hstack((a, b))
print(c)  # [1 2 3 4 5]


# Note that for 1D arrays, the input arrays can have different lengths as shown in the above example.
