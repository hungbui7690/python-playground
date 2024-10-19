"""
ZEROS
- The zeros() function of the numpy module allows you to create a numpy array of a given shape whose elements are filled with zeros.

"""

import numpy as np


# For example, the following uses the zeros() function to create an array with two axes, the first axis has two elements and the second axis has three elements:
a = np.zeros((2, 3))
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]]


# In layman’s terms, this example creates a 2-D array or a matrix that has two rows and three columns.
# By default, zeros() function uses the type float64 for its elements.
a = np.zeros((2, 3))
print(a.dtype)  # float64


# To use a different type, you need to explicitly specify it in the zeros() function via the dtype argument. For example:
a = np.zeros((2, 3), dtype=np.int32)
print(a)
# [[0 0 0]
#  [0 0 0]]
print(a.dtype)  # int32

# In this example, we use int32 type for the elements. Hence, you don’t see the decimal point (.) in the output.


# Summary
# Use numpy zeros() function to create an array of a given shape whose elements are filled with zeros.
