"""
SUM
- The numpy sum() function is an aggregate function that takes an array and returns the sum of all elements.

"""

import numpy as np


# The following example uses the sum() function to calculate the sum of all elements of a 2-D array:


a = np.array([[1, 2, 3], [4, 5, 6]])

total = np.sum(a)
print(total)  # 21


# In this example, the sum() adds up all the numbers of the array a.
# The sum() function also accepts the axis argument that allows you to return the sum of elements of an axis.
