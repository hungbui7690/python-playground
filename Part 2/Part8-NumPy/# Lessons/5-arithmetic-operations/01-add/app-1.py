"""
ADD

- The + or add() function of two equal-sized arrays perform element-wise additions. It returns the sum of two arrays, element-wise.

"""

import numpy as np


# The following example uses the + operator to add two 1-D arrays:
a = np.array([1, 2])
b = np.array([2, 3])

c = a + b
print(c)  # [3 5]

# [1+2, 2+3] = [3,5]
