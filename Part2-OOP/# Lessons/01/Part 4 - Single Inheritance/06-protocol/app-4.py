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


"""
- In this example, the Product and Stock class don’t need to subclass the Item class but still can be used in the calculate_total() function.

- This is called duck typing in Python. In duck typing, the behaviors and properties of an object determine the object type, not the explicit type of the object.

- For example, an object with the quantity and price will follow the Item protocol, regardless of its explicit type.

- The duck typing is inspired by the duck test:

    > If it walks like a duck and its quacks like a duck, then it must be a duck.

- In practice, when you write a function that accepts input, you care more about the behaviors and properties of the input, not its explicit type.



Summary
- Use Python Protocol to define implicit interfaces.

"""
