"""
STACK

"""

import numpy as np


# NumPy stack() vs. concatenate()
# The following example illustrates the difference between stack() and concatenate() functions: pic-2
a = np.array([1, 2])
b = np.array([3, 4])

c = np.concatenate((a, b))  # return 1-D array
d = np.stack((a, b))  # return 2-D array

print(c)  # [1 2 3 4]
print(d)
# [[1 2]
#  [3 4]]


# In this example, the concatenate() function joins elements of two arrays along an existing axis while the stack() function joins the two arrays along a new axis.


# Summary
# Use the numpy stack() function to join two or more arrays into one.
