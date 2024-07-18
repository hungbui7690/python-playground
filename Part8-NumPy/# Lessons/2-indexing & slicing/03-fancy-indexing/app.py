"""
FANCY INDEXING

Introduction to fancy indexing

- In the previous tutorial, you learned how to select elements from a numpy array using indexing and slicing techniques.
- Besides using indexing & slicing, NumPy provides you with a convenient way to index an array called fancy indexing.
- Fancy indexing allows you to index a numpy array using the following:

    Another numpy array
    A Python list
    A sequence of integers

"""

import numpy as np

a = np.arange(1, 10)
print(a)  # [1 2 3 4 5 6 7 8 9]

# this return the index 2,3,4 > we will use these indices below
indices = np.array([2, 3, 4])
print(a[indices])  # [3 4 5]


# Summary
# Fancy indexing allows you to index an array using another array, a list, or a sequence of integers.
