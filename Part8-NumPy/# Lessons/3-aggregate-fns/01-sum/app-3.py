"""
SUM
- The numpy sum() function is an aggregate function that takes an array and returns the sum of all elements.

"""

import numpy as np


# The sum() function also accepts the axis argument that allows you to return the sum of elements of an axis. For example:


a = np.array([[1, 2, 3], [4, 5, 6]])

total = np.sum(a, axis=0)  # pic-1
print(total)


# In this example, the sum() function returns a new array where each element is the sum of elements of the array a on axis-0.
# 1 + 4 = 5
# 2 + 5 = 7
# 3 + 6 = 9
# > 5 + 7 + 9 = 21
