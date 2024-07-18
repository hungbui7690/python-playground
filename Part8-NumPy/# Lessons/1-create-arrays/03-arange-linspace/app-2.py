"""
LINSPACE
- The numpy linspace() function creates a new numpy array with evenly spaced numbers over a given interval:

  @@ numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

- The linspace() works like the arange() function. But instead of specifying the step size, it defines the number of elements in the interval between the start and stop values.

"""

import numpy as np


# For example, the following uses the linspace() function to create a new array with five numbers between 1 and 2:
a = np.linspace(1, 2, 5)
print(a)  # [1.   1.25 1.5  1.75 2.  ]


# If you don’t want to include the stop value, you can exclude it using the endpoint parameter. For example:
a = np.linspace(1, 2, 5, endpoint=False)
print(a)  # [1.  1.2 1.4 1.6 1.8]


# Note that the endpoint is True by default. Therefore, the linspace() function returns the stop as the last sample by default.
