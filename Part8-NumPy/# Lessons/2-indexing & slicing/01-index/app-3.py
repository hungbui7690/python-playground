"""
INDEXING

NumPy array indexing on 3-D arrays

"""

import numpy as np


a = np.array(
    [
        [[1, 2], [3, 4], [5, 6]],
        [[5, 6], [7, 8], [9, 10]],
    ]
)

print(a.shape)  # (2, 3, 2)


print(a[0, 0, 1])  # 2
# The first number 0 selects the first element of the first axis so it returns:
# [[1, 2], [3, 4], [5, 6]]
# The second number 0 selects the first element of the second axis so it returns:
# [1, 2]
# The third number (1) selects the second element of the third axis which returns 2.
