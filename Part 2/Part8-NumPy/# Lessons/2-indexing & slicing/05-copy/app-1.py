"""
COPY

- When you slice an array, you get a subarray. The subarray is a view of the original array. In other words, if you change elements in the subarray, the change will be reflected in the original array.

"""

import numpy as np


# First, create a 2D array:
a = np.array([[1, 2, 3], [4, 5, 6]])


# Second, slice the array a and assign the subarray to the variable b:
b = a[0:, 0:2]
print(b)
# [[1 2]
#  [4 5]]


# Third, change the element at index [0,0] in the subarray b to zero and display the variable b:
b[0, 0] = 0
print(b)
# [[0 2]
#  [4 5]]


# Since b is a view of array a, the change is also reflected in array a:
print(a)
# [[0 2 3]
#  [4 5 6]]

# The reason numpy creates a view instead of a new array is that it doesn’t have to copy data therefore improving performance.
