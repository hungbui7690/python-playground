"""
ALL

- The numpy all() function returns True if all elements in an array (or along a given axis) evaluate to True.

- The following shows the syntax of the all() function:

    numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)

- In this syntax, a is a numpy array or an array-like object e.g., a list.

- If the input array contains all numbers, the all() function returns True if all numbers are nonzero or False if least one number is zero. The reason is that all non-zero numbers evaluate to True while zero evaluates to False.

"""

import numpy as np


# The following example uses the all() function to test whether all numbers in an array are non-zero:
result = np.all([0, 1, 2, 3])
print(result)  # False


# This example returns True because all numbers in the array are nonzero. You can pass an array-like object e.g., a list to the all() function. For example:
result = np.all(np.array([-1, 2, 3]))
print(result)  # True
