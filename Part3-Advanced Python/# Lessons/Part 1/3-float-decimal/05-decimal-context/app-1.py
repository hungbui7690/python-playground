"""
Decimal context

- Decimal always associates with a context that controls the following aspects:

    Precision during an arithmetic operation
    Rounding algorithm

- By default, the context is global. The global context is the default context. Also, you can set a temporary context that will take effect locally without affecting the global context.

- To get the default context, you call the getcontext() function from the decimal module:

      ~~ decimal.getcontext()

- The getcontext() function returns the default context, which can be global or local.

- To create a new context copied from another context, you use the localcontext() function:

      ~~ decimal.localcontext(ctx=None)

- The localcontext() returns a new context copied from the context ctx if specified.

- Once getting the context object, you can access the precision and rouding via the prec and rounding property respectively:

    ctx.pre: get or set the precision. The ctx.pre is an integer which defaults to 28
    ctx.rounding: get or set the rounding mechanism. The rounding is a string. It defaults to 'ROUND_HALF_EVEN'. Note floats also use this rounding mechanism.

- Python provides the following rounding mechanisms:

    Rounding	        Description
    ROUND_UP	        round away from zero
    ROUND_DOWN	      round towards zero
    ROUND_CEILING	    round to ceiling (towards positive infinity)
    ROUND_FLOOR	      round to floor (towards negative infinity)
    ROUND_HALF_UP	    round to nearest, ties away from zero
    ROUND_HALF_DOWN	  round to nearest, ties towards zero
    ROUND_HALF_EVEN	  round to nearest, ties to even (least significant digit)

"""

# This example illustrates how to get the default precision and rounding of the default context:
from decimal import Decimal
import decimal

ctx = decimal.getcontext()

print(ctx.prec)  # 28
print(ctx.rounding)  # ROUND_HALF_EVEN


# The following example shows how the 'ROUND_HALF_EVEN' rounding mechanism takes effect:
x = Decimal("2.25")
y = Decimal("3.35")

print(round(x, 1))  # 2.2
print(round(y, 1))  # 3.4
