"""
Type aliases


"""

# Python allows you to assign an alias to a type and use the alias for type hintings. For example:

from typing import Union


number = Union[int, float]  # Type Alias


def add(x: number, y: number) -> number:
    return x + y


# In this example, we assign the Union[int, float] type an alias Number and use the Number alias in the add() function.
