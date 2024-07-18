"""
MEAN
- The mean() function returns the average of elements in an array. Here’s the syntax of the mean() function:

    numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where= <no value>)

- In this syntax:

    a is an array that you want to calculate the average of elements.
    axis is the axis if specified will return the average of elements on that axis.

"""

import numpy as np


# 1) Using NumPy mean() function on 1-D array


a = np.array([1, 2, 3])
average = np.mean(a)
print(average)  # 2.0


# The output is 2.0 because (1 + 2 + 3) / 3 = 2.0
