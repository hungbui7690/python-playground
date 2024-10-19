"""
PROD

- Suppose you have three numbers n, m, and k. The product of the three numbers is nxmxk. For example, the product of 2, 3, and 4 is 2x3x4 = 24.

- To calculate the products of numbers in an array, you use the numpy prod() function:

    numpy.prod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial = <no value>, where = <no value>)


"""

import numpy as np


# 1) Using the numpy prod() function with 1-D array example


# The following example uses the prod() to calculate the products of numbers in a 1-D array:
a = np.arange(1, 5)
result = np.prod(a)

print(a)  # [1 2 3 4]
print(f"result={result}")  # result=24


# Note that you can pass an array like object to the prod() function e.g., a list. For example:
result = np.prod([1, 2, 3, 4, 5])
print(f"result={result}")  # result=120
