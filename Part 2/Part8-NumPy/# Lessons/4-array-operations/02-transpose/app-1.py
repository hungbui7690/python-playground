"""
TRANSPOSE
- The numpy transpose() function reverses the axes of an array. Here’s the syntax of the transpose() function:

    numpy.transpose(a, axes=None)

- In this syntax:

    a is an input array. It can be a numpy array or any object that can be converted to a numpy array.
    axes is a tuple or a list that contains a permutation of [0,1,..,N-1] where N is the number of axes of the array a.

- The transpose() function returns the array a with its axes permuted.

- The transpose() function is equivalent to:

    ndarray.T property method that returns an array transposed.
    ndarray.transpose(*axes) method that returns an array transposed.

"""

import numpy as np


# The following example uses the transpose() function with 1-D array:
a = np.array([1, 2, 3])
b = np.transpose(a)
print(b)  # [1 2 3]


# The transpose() function has no effect on a 1-D array because a transposed vector is simply the same vector.
