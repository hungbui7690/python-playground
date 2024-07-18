"""
Shape
- pic

"""

import numpy as np


# Getting shapes of arrays
# To find the number of axes and the number of elements on each axis of an array, you use the shape property.
a = np.array([1, 2, 3])
print(a.shape)  # (3,)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)  # (2, 3)

c = np.array(
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]],
    ]
)
print(c.shape)  # (2, 2, 3)


# The shape property returns a tuple:
# The number of elements in the tuple is the number of axes.
# Each tuple element stores the number of elements of the corresponding axis.


# Summary
# A numpy array is a grid of values with the same type and is indexed by a tuple of non-negative values.
# Numpy arrays have the type of ndarray.
# Use the array() function to create a numpy array.
# Use the dtype property to get the data type of array’s elements.
# Use the ndim property to get the number of dimensions or the number of axes.
# Use the shape property to get the number of dimensions as well as the number of elements in each dimension.
