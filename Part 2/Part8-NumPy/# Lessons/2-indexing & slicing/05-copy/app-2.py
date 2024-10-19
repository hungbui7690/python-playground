"""
COPY

- When you slice an array, you get a subarray. The subarray is a view of the original array. In other words, if you change elements in the subarray, the change will be reflected in the original array.

"""

import numpy as np


# However, if you want a copy of an array rather than a view, you can use copy() method. For example:


a = np.array([[1, 2, 3], [4, 5, 6]])

# make a copy
b = a[0:, 0:2].copy()
print(b)
# [[1 2]
#  [4 5]]


b[0, 0] = 0
print(b)
# [[0 2]
#  [4 5]]

print(a)
# [[1 2 3]
#  [4 5 6]]


# In this example:
# First, call the copy() method of array a to make a copy of a subarray and assign it to the variable b.
# Second, change the element at index [0,0] of the array b, because both arrays are independent, the change doesn’t affect array a.


# Summary
# When you slice an array, you’ll get a view of the array.
# Use the copy() method to make a copy of an array rather than a view.
