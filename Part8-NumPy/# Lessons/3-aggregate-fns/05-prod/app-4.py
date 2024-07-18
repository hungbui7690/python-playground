"""
PROD


"""

import numpy as np


# 4) Special cases


# Note that if you pass an array of integers to the prod() function that causes an overflow, the prod() won’t raise the error. For example:
result = np.prod(np.arange(1, 100))
print(f"result={result}")  # result=0


# The prod() function returns 1 if the array is empty. For example:
result = np.prod(np.array([]))
print(f"result={result}")  # result=1.0
