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

# If you change the rounding to 'ROUND_HALF_UP', you’ll get a different result:
import decimal
from decimal import Decimal


ctx = decimal.getcontext()
ctx.rounding = decimal.ROUND_HALF_UP

x = Decimal("2.25")
y = Decimal("3.35")

print(round(x, 1))  # 2.3
print(round(y, 1))  # 3.4
