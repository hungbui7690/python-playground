"""
FLATTEN

"""

import numpy as np


#
a = np.array([[1, 2], [3, 4]])
b = a.flatten()


b[0] = 0
print(b)  # [0 2 3 4]

print(a)
# [[1 2]
#  [3 4]]


# The output shows that the element at index 0 of b changes but the element at index 0 of a doesn’t change.s
