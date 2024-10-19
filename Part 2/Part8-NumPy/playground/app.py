"""
SPLIT

"""

import numpy as np


# 3) Using the NumPy split() function using indices
# The following example uses the split() function to split a 1D array using an array of indices:
a = np.arange(10, 70, 10)
results = np.split(a, [2, 3, 4])
print(a)  # [10 20 30 4500  60]
print(results)
# [array([10, 20]), array([30]), array([40]), array([50, 60])]
