"""
RAVEL

- The ravel() function accepts an array and returns a 1-D array containing the elements of the input array:

    numpy.ravel(a, order='C')

- In this syntax:

    + a is a numpy array. It can be any array-like object e.g., a list. An array-like object is an object that can be converted into a numpy array.
    + order specifies the order of elements. Check out the flatten() method for detailed information on the order parameter and its values.

"""

import numpy as np


# The following example uses the ravel() function to flatten a 2-D array:
a = np.array([[1, 2], [3, 4]])
b = np.ravel(a)

print(b)  # [1 2 3 4]
