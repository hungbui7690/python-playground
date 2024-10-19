"""
VSTACK


"""

import numpy as np


# The following example attempts to join elements of two 1D arrays with different lengths and causes an error:
a = np.array([1, 2])
b = np.array([3, 4, 5])

c = np.vstack((a, b))
print(c)
# d the array at index 1 has size 3
