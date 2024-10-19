"""
PROD

- Suppose you have three numbers n, m, and k. The product of the three numbers is nxmxk. For example, the product of 2, 3, and 4 is 2x3x4 = 24.

- To calculate the products of numbers in an array, you use the numpy prod() function:

    numpy.prod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial = <no value>, where = <no value>)


"""

import numpy as np


# 2) Using the numpy prod() function with multidimensional array examples

# The following example uses the prod() to calculate products of all numbers in a 2-D array:
result = np.prod([[1, 2], [3, 4]])

print(f"result={result}")  # result=24


# To calculate product of numbers of an axis, you can specify the axis argument. For example, the following uses the prod() to calculate the product of numbers on axis 0:
result = np.prod([[1, 2], [3, 4]], axis=0)

print(f"result={result}")  # result=[3 8]


# Similarly, you can calculate the product of numbers on axis 1:
result = np.prod([[1, 2], [3, 4]], axis=1)

print(f"result={result}")  # result=[ 2 12]
