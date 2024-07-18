"""
SPLIT

"""

import numpy as np


# 2) Using the split() function to split a 2D array
# The following example uses the split() function to split a 2D array into two subarrays:
a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
results = np.split(a, 2)

print(a)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


print(results)
# [array([[1, 2],
#        [3, 4]]),
# array([[5, 6],
#        [7, 8]])]
