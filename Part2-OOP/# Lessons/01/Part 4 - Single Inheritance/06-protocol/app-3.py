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


class Item(Protocol):
    quantity: float
    price: float


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


# For example, you can define a list of stocks in inventory and pass them to the calculate_total() function:
class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


# calculate total an inventory list
total = calculate_total([Stock("Tablet", 5, 950), Stock("Laptop", 10, 850)])

print(total)  # 13250
