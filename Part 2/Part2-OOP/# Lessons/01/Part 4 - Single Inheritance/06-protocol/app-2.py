"""
Python Protocol
- to define implicit interfaces.

"""

from typing import List, Protocol


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


# The following describes how to use the Protocol class.
# First, define an Item class that inherits from the Protocol with two attributes: quantity and price:
class Item(Protocol):
    quantity: float
    price: float


# Second, change the calculate_total() function that accepts a list of Item objects instead of a list of Product objects:
def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# By doing this, you can pass any list of Item objects to the calculate_total() function with the condition that each item has two attributes quantity and price.


# # calculate total a product list
total = calculate_total([Product("A", 10, 150), Product("B", 5, 250)])
print(total)  # 2750
