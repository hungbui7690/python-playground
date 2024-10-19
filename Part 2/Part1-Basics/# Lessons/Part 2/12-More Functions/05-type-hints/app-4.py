"""
Adding type hints for multiple types

- The following add() function returns the sum of two numbers:

        def add(x, y):
            return x + y

- The numbers can be integers or floats. You can use the module to set type hints for multiple types.


~~ mypy app.py


"""

# First, import Union from typing module:
from typing import Union


# Second, use the Union to create a union type that includes int and float:
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


# Starting from Python 3.10, you can use the X | Y syntax to create a union type, for example:
def addX(x: int | float, y: int | float) -> int | float:
    return x + y
