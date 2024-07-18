"""
STACK

"""

import numpy as np


# 2) Using numpy stack() function to join 2D arrays
# The following example uses the stack() function to join elements of two 2D arrays. The result is a 3D array:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.stack((a, b))  # pic-1
print(c)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]

print(c.shape)  # (2, 2, 2)
