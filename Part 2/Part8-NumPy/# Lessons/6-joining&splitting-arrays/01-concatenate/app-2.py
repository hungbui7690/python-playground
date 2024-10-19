"""
CONCATENATE

"""

import numpy as np


# 2) Using the concatenate() function to join two 2D arrays
# The following example uses the concatenate() function to join two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.concatenate((a, b))
print(c)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# The output shows that the concatenate() function joins two arrays vertically because by default the axis argument is zero.


# If the axis is one, the concatenate() function will join two arrays horizontally. For example:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.concatenate((a, b), axis=1)
print(c)
# [[1 2 5 6]
#  [3 4 7 8]]


# Summary
# Use the numpy concatenate() function to join elements of a sequence of arrays into a single array.
