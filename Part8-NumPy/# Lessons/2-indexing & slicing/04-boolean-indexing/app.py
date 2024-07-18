"""
BOOLEAN INDEXING

- Numpy allows you to use an array of boolean values as an index of another array. Each element of the boolean array indicates whether or not to select the elements from the array.

- If the value is True, the element of that index is selected. In case the value is False, the element of that index is not selected.

"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([True, True, False])
c = a[b]
print(c)  # [1 2]
# Because the first and second elements of the array b are True, the a[b] returns a new array with the first and second elements of the array a.


# Typically, you’ll use boolean indexing to filter an array. For example:

a = np.arange(1, 10)
b = a > 5
print(b)  # [False False False False False  True  True  True  True]

c = a[b]
print(c)  # [6 7 8 9]
