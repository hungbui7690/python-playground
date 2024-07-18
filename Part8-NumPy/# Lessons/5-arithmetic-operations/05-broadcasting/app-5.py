"""
BROADCASTING

NumPy broadcasting rules

- NumPy defines a set of rules for broadcasting:

    + Rule 1: if two arrays have different dimensions, it pads ones on the left side of the shape of the array that has fewer dimensions.
    + Rule 2: if two dimensions of arrays do not match in any dimension, the array with a shape equal to one in that dimension is stretched (or broadcast) to match the shape of another array.
    + Rule 3: if any dimension of two arrays is not equal and neither is equal to one, NumPy raises an error.

"""

import numpy as np


# 3) NumPy broadcasting with error example
# The following example adds two arrays that are not compatible:
a = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
)
print("a shape: ", a.shape)  # a shape:  (3, 2)

b = np.array([1, 2, 3])
print("b shape: ", b.shape)  # b shape:  (3,)

c = a + b  # ValueError: operands could not be broadcast together with shapes (3,2) (3,)


"""
In this example, the array a and b have the following shapes:

  Array	  Shape
  a	      (3,2)
  b	      (3,)

By rule 1, NumPy pads the shape of the second array with ones:

  Array	  Shape
  a	      (3,2)
  b	      (1,3)

By rule 2, NumPy stretches the first dimension of the b array from 1 to 3 to match:

  Array	  Shape
  a	      (3,2)
  b	      (3,3)

By rule 3, the final shapes do not match, therefore, NumPy raises an error.
"""


# Summary
# NumPy broadcasting is a set of rules for applying arithmetic operations on arrays of different shapes.
