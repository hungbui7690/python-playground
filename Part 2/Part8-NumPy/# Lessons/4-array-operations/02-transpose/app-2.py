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


# The following example uses the transpose() function to transpose a 2-D array (or a matrix):
a = np.array([[1, 2, 3], [4, 5, 6]])

b = np.transpose(a)
print(b)
# [[1 4]
#  [2 5]
#  [3 6]]


# In this example, the transpose() function transpose a (2,3) array. Basically, it swaps rows and columns of the array.
# After the transposition, the first row of array a becomes the first column of the transposed array b, the second row of array a becomes the second column of the transposed array b.
