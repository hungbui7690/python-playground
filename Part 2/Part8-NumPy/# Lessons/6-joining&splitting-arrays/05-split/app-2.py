"""
SPLIT

"""

import numpy as np


# The following example raises an error because the split is not possible:
a = np.arange(1, 7)
# [1 2 3 4 5 6]

results = np.split(a, 4)
# ValueError: array split does not result in an equal division


# In this example, the array has 6 elements therefore it cannot be split into 4 arrays of equal size. If you want to have a more flexible split, you can use the array_split() function.
