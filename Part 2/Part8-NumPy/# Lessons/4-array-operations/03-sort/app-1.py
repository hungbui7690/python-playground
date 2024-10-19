"""
SORT
- The sort() function returns a sorted copy of an array. Here’s the syntax of the sort() function:

    numpy.sort(a, axis=- 1, kind=None, order=None)

- In this syntax:

    - a is a numpy array to be sorted. Also, it can be any object that can be converted to an array.
    - axis specifies the axis along which the elements will be sorted. If the axis is None, the function flattens the array before sorting. By default, the axis is -1 which sorts elements along the last axis.
    - kind specifies the sorting algorithm which can be ‘quicksort’, ‘mergesort’, ‘heapsort’, and ‘stable’.
    order specifies which fields to compare first, second, etc when sorting an array with fields defined. The order can be a string that represents the field to sort or a list of strings that represent a list of fields to sort.

- If you want to sort the elements of an array in place, you can use the sort() method of the ndarray object with the following syntax:

    ndarray.sort(axis=- 1, kind=None, order=None)

"""

import numpy as np


# The following example uses the sort() function to sort numbers in a 1-D array:
a = np.array([2, 3, 1])
b = np.sort(a)
print(b)  # [1 2 3]


# In this example, the sort() function sorts the elements of the array from low to high.
