"""
SPLIT
- The split() function splits an array into multiple sub-arrays as views. The syntax of the split() function is as follows:

    numpy.split(ary, indices_or_sections, axis=0)

- In this syntax:

    + ary is the array to be split into subarrays.
    + indices_or_sections can be an integer or a 1-D array of sorted integers.
      > If it is an integer, the function splits the input array into N equal arrays along the axis. If the split is not possible, the function will raise an error.
      > If indices_or_sections is a 1D array of sorted integers, the indices indicate where along the axis the function splits the array.

- When an index exceeds the dimension of the array along the axis, the function returns an empty subarray.
- The following picture shows how the split() function splits the array with indices 2, 3, and 4. It results in 4 arrays. pic

"""

import numpy as np


# 1) Using the split() function to split a 1D array
# The following example uses the split() function to split a 1D array with seven elements into three sub-arrays:
a = np.arange(1, 7)
results = np.split(a, 3)

print(a)  # [1 2 3 4 5 6]
print(results)  # [array([1, 2]), array([3, 4]), array([5, 6])]
