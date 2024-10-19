"""
ANY
- The numpy any() function returns True if any element in an array (or along a given axis) evaluates to True.

- Here’s the syntax of the any function:

    numpy.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)

- In this syntax, a is a numpy array or any object that can be converted to an array e.g., a list.

- Typically, the input array contains numbers. In the boolean context, all non-zero numbers evaluate to True while zero evaluates to False. Therefore, the any() function returns True if any number in the array is nonzero or False if all numbers are zero.

"""

import numpy as np


# The following example uses the any() function to test whether any number in an array are non-zero:
result = np.any([0, 1, 2, 3])
print(result)  # True
# The result is True because the array of three non-zero numbers.


# This example returns False because all numbers in the array are zero. In fact, you can pass any object that can be converted into a list to the any() function. For example:
result = np.any([0, 0])
print(result)  # False
