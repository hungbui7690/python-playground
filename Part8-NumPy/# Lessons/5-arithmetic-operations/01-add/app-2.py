"""
ADD

- The + or add() function of two equal-sized arrays perform element-wise additions. It returns the sum of two arrays, element-wise.

"""

import numpy as np


# Similarly, you can use the add() function to add two 1D arrays using "np"
a = np.array([1, 2])
b = np.array([2, 3])

c = np.add(a, b)

print(c)  # [3 5]


# [1+2, 2+3] = [3,5]
