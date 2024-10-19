"""
BROADCASTING

NumPy broadcasting rules

- NumPy defines a set of rules for broadcasting:

    + Rule 1: if two arrays have different dimensions, it pads ones on the left side of the shape of the array that has fewer dimensions.
    + Rule 2: if two dimensions of arrays do not match in any dimension, the array with a shape equal to one in that dimension is stretched (or broadcast) to match the shape of another array.
    + Rule 3: if any dimension of two arrays is not equal and neither is equal to one, NumPy raises an error.

"""

import numpy as np


# 1) NumPy broadcasting on one array example
# The following example adds a 2-D array to a 1D array:
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.ones(3)
c = a + b
print(c)
# [[2. 3. 4.]
#  [5. 6. 7.]]


"""
  The following table shows the shapes of a and b:

    Array	  Shape
    a	      (2,3)
    b	      (3,)

  By rule 1, because the array b has fewer dimensions, NumPy pads one on the left:

    Array	  Shape
    a	      (2,3)
    b	      (1,3)

  By rule 2, the first dimensions of two shapes are not equal, NumPy stretches (or broadcasts) the first dimension of the array b to match:

    Array	  Shape
    a	      (2,3)
    b	      (2,3)

  Now, the dimensions of both arrays match. The shape of the result array is (2,3).
"""
