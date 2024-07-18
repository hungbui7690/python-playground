"""
RESHAPE

- A shape of an array stores the number of dimensions (or axes) and the number of elements on each dimension. The shape property returns a tuple that describes the shape of an array.
- The reshape() function changes the shape of an array without changing its elements. Here’s the syntax of the reshape() function:

    numpy.reshape(a, newshape, order='C')

- In this syntax, the reshape() function changes the shape of the array a to the newshape but keep the number of elements the same.
- The reshape() function is equivalent to calling the reshape() method on the array a:

    a.reshape(newshape, order='C')

"""

import numpy as np


# The following example uses the numpy reshape() function to change a 1-D array with 4 elements to a 2-D array:
a = np.arange(1, 5)
print(a)  # [1 2 3 4]

b = np.reshape(a, (2, 2))
print(b)
# [[1 2]
#  [3 4]]
