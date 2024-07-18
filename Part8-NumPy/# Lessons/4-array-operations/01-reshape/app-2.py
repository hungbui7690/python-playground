"""
RESHAPE


"""

import numpy as np


# Note that array b is a view of array a. It means that if you change an element of array b, the change is reflected in array a. For example:
a = np.arange(1, 5)
b = np.reshape(a, (2, 2))

b[0, 0] = 0

print(b)
# [[0 2]
#  [3 4]]

print(a)  # [0 2 3 4]


# In this example, we change the element at index [0,0] in the array b. The change is also reflected in the array a.


# Summary
# Use the numpy reshape() function to change the shape of an array without changing its elements.
# You can change the shape of an array as long as the number of elements is the same.
