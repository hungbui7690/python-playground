"""
ONES
- The ones() function of the numpy module allows you to create a numpy array of a given shape whose elements are filled with ones.

"""

import numpy as np


# For example, the following uses the ones() function to create an array with three axes, the first axis has two elements, the second axis has three elements, and the third axis has 4 elements:
a = np.ones((2, 3, 2))
print(a)
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]

#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]


# By default, ones() function uses float64 for its elements. For example:
print(a.dtype)  # float64


# To use a different type, you need to specify it using the dtype argument. For example:
a = np.ones((2, 3, 4), dtype=np.int32)
print(a.dtype)  # int32
