"""
SORT

"""

import numpy as np


# To sort elements of an array from high to low, you can use the sort() function to sort an array from low to high and use a slice to reverse the array. For example:
a = np.array([2, 3, 1])
b = np.sort(a)[::-1]
print(b)  # [3 2 1]


# In this example:
# First, the sort() function sorts the elements in the array a in ascending order (from low to high)
# Then, the slice [::-1] reverses the sorted array so that the elements of the result array are in descending order.
