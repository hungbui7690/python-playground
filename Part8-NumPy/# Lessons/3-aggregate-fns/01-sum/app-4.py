"""
SUM
- The numpy sum() function is an aggregate function that takes an array and returns the sum of all elements.

"""

import numpy as np


# Similarly, you can sum elements on axis-1 like this:


a = np.array([[1, 2, 3], [4, 5, 6]])

total = np.sum(a, axis=1)  # pic-2
print(total)  # 21


# 1 + 2 + 3 = 6
# 4 + 5 + 6 = 15
# > 6 + 15 = 21


# Summary
# Use the sum() function to get the sum of all elements of an array.
# Use the axis argument to specify the axis that you want to sum up.
