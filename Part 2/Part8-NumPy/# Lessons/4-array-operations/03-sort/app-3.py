"""
SORT

"""

import numpy as np


# The following example uses the sort() function to sort a 2-D array:
a = np.array([[2, 3, 1], [5, 6, 4]])
b = np.sort(a)
print(b)
# [[1 2 3]
#  [4 5 6]]


# The following example uses the sort() function to sort elements on axis 0:
a = np.array([[5, 3, 4], [2, 6, 1]])
b = np.sort(a, axis=0)  # pic-1
print(b)
# [[2 3 1]
#  [5 6 4]]


# Similarly, you can sort elements of the array on axis 1:
a = np.array([[5, 3, 4], [2, 6, 1]])
b = np.sort(a, axis=1)  # pic-2
print(b)
# [[3 4 5]
#  [1 2 6]]
