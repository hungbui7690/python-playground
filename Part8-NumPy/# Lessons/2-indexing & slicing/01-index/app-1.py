"""
INDEXING

NumPy array indexing on 1-D arrays

- Along a single axis, you can select elements using indices. The first element starts with index 0, the second element starts with index 1, and so on.
- Besides the non-negative indices, you can use negative indices to locate elements. For example, the last element has an index -1, the second last element has an index -2, and so on.

"""

import numpy as np


a = np.arange(0, 5)
print(a)  # [0 1 2 3 4]
print(a[0])  # 0
print(a[1])  # 1
print(a[-1])  # 4
