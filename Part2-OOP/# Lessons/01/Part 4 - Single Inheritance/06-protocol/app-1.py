"""
Python Protocol
- to define implicit interfaces.

"""

from typing import List


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


# Suppose you have a function that calculates the total value of a product list, where each product has the name, quantity, and price attributes:
def calculate_total(items: List[Product]) -> float:
    return sum([item.quantity * item.price for item in items])


# In this example, the calculate_total() function accepts a list of Product objects and returns the total value.
# When writing this function, you may want to calculate the total of a product list. But you likely want to use it for other lists such as inventory lists in the future.
# If you look closely at the calculate_total() function, it only uses the quantity and price attributes.
# To make the calculate_total() more dynamic while leveraging type hints, you can use the Protocol from the typing module. The Protocol class has been available since Python 3.8, described in PEP 544.
