"""
DIVIDE

- The / operator or divide() function returns the quotient of two equal-sized arrays by performing element-wise division.

"""

import numpy as np


# The following example uses the / operator to find the quotient of two 1-D arrays:
a = np.array([8, 6])
b = np.array([2, 3])
c = a / b
print(c)  # [4. 2.]


# Similarly, you can use the divide() function to get the quotient of two 1D arrays as follows:
c = np.divide(a, b)
print(c)  # [4. 2.]
