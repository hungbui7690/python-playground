"""
Decimal context

    Rounding	        Description
    ROUND_UP	        round away from zero
    ROUND_DOWN	      round towards zero
    ROUND_CEILING	    round to ceiling (towards positive infinity)
    ROUND_FLOOR	      round to floor (towards negative infinity)
    ROUND_HALF_UP	    round to nearest, ties away from zero
    ROUND_HALF_DOWN	  round to nearest, ties towards zero
    ROUND_HALF_EVEN	  round to nearest, ties to even (least significant digit)

"""

# The following example shows you how to copy the default context and change the rounding to 'ROUND_HALF_UP':

import decimal
from decimal import Decimal


x = Decimal("2.25")
y = Decimal("3.35")

with decimal.localcontext() as ctx:
    print("Local context:")
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))  # 2.3
    print(round(y, 1))  # 3.4

print("Global context:")
print(round(x, 1))  # 2.2
print(round(y, 1))  # 3.4

# Notice that the local context doesn’t affect the global context. After the with block, Python uses the default rounding mechanism.
