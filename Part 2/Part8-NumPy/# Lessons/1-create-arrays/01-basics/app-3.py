"""
Create NumPy Array

"""

import numpy as np


# Creating two-dimensional arrays (matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)  # [[1 2 3] [4 5 6]]
print(b.ndim)  # 2


# Creating three-dimensional array
c = np.array(
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]],
    ]
)

print(c.ndim)  # 3
