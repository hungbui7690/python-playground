"""
BROADCASTING
- In previous tutorials, you learned how to perform arithmetic operations on equal-sized arrays using the add(), subtract(), multiply(), and divide() functions or as +, -, *, and / operators.

- To perform arithmetic operations on arrays of different shapes, NumPy uses a technique called broadcasting.

- By definition, broadcasting is a set of rules for applying arithmetic operations on arrays of different shapes. We’ll cover these rules in detail shortly.

"""

import numpy as np


# Before that, let’s take some simple broadcasting examples. For instance, you can use the + operator to add a number to an array like this:
a = np.array([1, 2, 3])
b = a + 1
print(b)  # [2 3 4]

# This example adds the number one to a 1D array using the operator +. Internally, NumPy adds the number 1 to every element of the array. This technique is called broadcasting.
# In other words, NumPy broadcasts the number one across the first dimension to match the shape of the 1D array.


# Conceptually, you can think of the above broadcasting as equivalent to the following: pic
a = np.array([1, 2, 3])
b = a + np.array([1, 1, 1])
print(b)
