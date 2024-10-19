"""
BROADCASTING

NumPy broadcasting rules

- NumPy defines a set of rules for broadcasting:

    + Rule 1: if two arrays have different dimensions, it pads ones on the left side of the shape of the array that has fewer dimensions.
    + Rule 2: if two dimensions of arrays do not match in any dimension, the array with a shape equal to one in that dimension is stretched (or broadcast) to match the shape of another array.
    + Rule 3: if any dimension of two arrays is not equal and neither is equal to one, NumPy raises an error.

"""

import numpy as np


# 2) NumPy broadcasting on both arrays example
# The following example illustrates the case where NumPy broadcasts both arrays:
a = np.array(
    [
        [1],
        [2],
        [3],
    ]
)
print("a shape: ", a.shape)  # a shape:  (3, 1)

b = np.array([1, 2, 3])
print("b shape: ", b.shape)  # b shape:  (3,)

c = a + b
print(c)
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]

print("c shape: ", c.shape)  # c shape:  (3, 3)


"""
In this example, the shape of a and b arrays are (3,1) and (3,) respectively.

  Array	  Shape
  a	      (3,1)
  b	      (3,)

By rule 1, NumPy pads the shape of b with ones:

  Array	  Shape
  a	      (3,1)
  b	      (1,3)

By rule 2, NumPy stretches the dimensions of both arrays a and b to match because they’re both ones:

  Array	  Shape
  a	      (3,3)
  b	      (3,3)

The resulting array has the shape of (3,3).
"""
