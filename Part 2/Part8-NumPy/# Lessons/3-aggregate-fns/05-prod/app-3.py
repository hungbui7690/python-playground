"""
PROD


"""

import numpy as np


# 3) Selecting numbers to include in the product


# To select specific number to include in the product, you use the where argument. For example:
a = np.array([np.nan, 3, 4])
result = np.prod(a, where=[False, True, True])
print(result)  # 12.0


# In this example, the array contains three elements np.nan, 3, and 4.
# The where argument uses a boolean list to specify which element in the array a should be included in the product.
# If the value of the where list is True, the corresponding element of the input array will be included in the product.
