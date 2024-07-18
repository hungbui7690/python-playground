"""
SLICING

Numpy array slicing on multidimensional arrays

- To slice a multidimensional array, you apply the square brackets [] and the : notation to each dimension (or axis). The slice returns a reduced array where each element matches the selection rules.

"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


print(a[0:2, :])
# [[1 2 3]
#  [4 5 6]]

"""
In this example, array a is a 2-D array. In the expression a[0:2, :]:
- First, the 0:2 selects the element at index 0 and 1, not 2 that returns:

    [[1 2 3]
    [4 5 6]]

- Then, the : select all elements. Therefore the whole expression returns:

    [[1 2 3]
    [4 5 6]]
"""


# Another Example
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a[1:, 1:])
# [[5 6]
#  [8 9]]

"""
In the expression a[1:, 1:]:
- First, 1: selects the elements starting at index 1 to the last element of the first axis (or row), which returns:

    [[4 5 6]
    [7 8 9]]

- Second, 1: selects the elements starting at index 1 to the last elements of the second axis (or column), which returns:

    [[5 6]
    [8 9]]
"""


# Summary
# Use slicing to extract elements from a numpy array
# Use a[m:n:p] to slice one-dimensional arrays.
# Use a[m:n:p, i:j:k, ...] to slice multidimensional arrays
