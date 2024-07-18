"""
Create NumPy Array
- The array is the core data structure of the NumPy library. A NumPy array is a grid of values with the same type and indexed by a tuple of non-negative integers.
- All arrays are instances of the ndarray class. To create a new NumPy array, you use the array() function of the NumPy library.

"""

import numpy as np


# 1. Creating one-dimensional arrays
a = np.array([1, 2, 3])

print(type(a))  # <class 'numpy.ndarray'>
print(a)  # [1 2 3]


# 2. Getting the dimension of an array
print(a.ndim)  # 1


# 3. Getting the data type of array elements
print(a.dtype)  # int64


# 4. In this example, the type of the elements is int64. If you want to set the type of the array’s elements, you can use the dtype argument of the array() function
a = np.array([1, 2, 3], dtype=np.float32)
print(a)  # [1. 2. 3.]
print(a.dtype)  # float32
