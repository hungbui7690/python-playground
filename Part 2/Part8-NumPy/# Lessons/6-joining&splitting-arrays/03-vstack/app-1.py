"""
VSTACK
- The vstack() function joins elements of two or more arrays into a single array vertically (row-wise).

- Here’s the syntax of the vstack() function:

    numpy.vstack((a1,a2,...))

- In this syntax, the (a1, a2, …) is a sequence of arrays with the ndarray type.
- All arrays a1, a2, .. must have the same shape along all but the first axis. If they’re 1D arrays, then they must have the same length.

"""

import numpy as np


# 1) Using vstack() function to join elements of 1D arrays
# The following example uses the vstack() function to join two 1D arrays vertically:
a = np.array([1, 2])
b = np.array([3, 4])

c = np.vstack((a, b))
print(c)
# [[1 2]
#  [3 4]]
