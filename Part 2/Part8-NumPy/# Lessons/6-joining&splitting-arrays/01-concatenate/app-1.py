"""
CONCATENATE

- The concatenate() function allows you to join two or more arrays into a single array. Here’s the basic syntax of the concatenate() function:

    np.concatenate((a1,a2,...),axis=0)

- In this syntax, the concatenate() function joins the elements of the sequence of arrays (a1, a2, …) into a single array. The arrays in the sequence must have the same shape.
- The axis specifies the axis along which the function will join the arrays. If the axis is None, the function will flatten the arrays before joining.
- The concatenate() function returns the concatenated array.

"""

import numpy as np


# 1) Using the concatenate() function to join two 1D arrays
# The following example uses the concatenate() function to join elements of two 1D arrays:
a = np.array([1, 2])
b = np.array([3, 4])
c = np.concatenate((a, b))
print(c)  # [1 2 3 4]


# In this example, the concatenate() function joins the elements in the array a and b into a single array c.
