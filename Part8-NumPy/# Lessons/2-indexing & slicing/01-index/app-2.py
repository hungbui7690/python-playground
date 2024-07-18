"""
INDEXING

NumPy array indexing on 2-D arrays

- With 2-D and multidimensional arrays, you can select elements as you do with 1-D arrays but for each dimension (or axis).

"""

import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)

print(a[0])  # [1 2 3]
print(a[1])  # [4 5 6]

print(a[0, 0])  # 1
print(a[1, 0])  # 4
print(a[0, 2])  # 3
print(a[1, 2])  # 6
print(a[0, -1])  # 3
print(a[1, -1])  # 6
