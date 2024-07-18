"""
FLATTEN

"""

import numpy as np


# The following example uses the numpy flatten() method to flatten an array using column-major order:
a = np.array([[1, 2], [3, 4]])
b = a.flatten(order="F")

print(b)  # [1 3 2 4]


# Summary
# Use the numpy array flatten() method to return a copy of an array collapsed into one dimension.
