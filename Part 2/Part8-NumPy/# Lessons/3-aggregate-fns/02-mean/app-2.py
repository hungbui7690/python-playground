"""
MEAN
- The mean() function returns the average of elements in an array. Here’s the syntax of the mean() function:

    numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where= <no value>)

- In this syntax:

    a is an array that you want to calculate the average of elements.
    axis is the axis if specified will return the average of elements on that axis.

"""

import numpy as np


# 2) Using NumPy mean() function on 2-D array
# The following example uses the mean() function to calculate the average of elements on axis-0:


a = np.array([[1, 2, 3], [4, 5, 6]])
average = np.mean(a, axis=0)
print(average)  # [2.5 3.5 4.5]


# (1 + 4) / 2 = 2.5
# (2 + 5) / 2 = 3.5
# (3 + 6) / 2 = 4.5
