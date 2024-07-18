"""
BROADCASTING

"""

import numpy as np


# However, NumPy broadcasts number one without duplicating it. By doing this, NumPy can manage efficiently and speeds up calculation in most cases.

# Similarly, you can add a 1D array to a 2D array using broadcasting like this:
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
c = a + b
print(c)
# [[11 22 33]
#  [14 25 36]]


# In this example, NumPy broadcasts the 1D array b across the second dimension to match the shape of the array a.
