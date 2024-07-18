"""
STACK

"""

import numpy as np


# The following example uses the stack() function to join two 1D arrays horizontally by using axis 1:
a = np.array([1, 2])
b = np.array([3, 4])

c = np.stack((a, b), axis=1)
print(c)
# [[1 3]
#  [2 4]]
