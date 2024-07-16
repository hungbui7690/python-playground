"""
float

"""


# 3) Using the Python float() to convert an object to a floating point number
# The following example illustrates how to convert an object to a floating point number:


# First, define a class Product that has two attributes name and price. The __float__() method returns the floating point number of the price:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __float__(self):
        return float(self.price)


# Second, create a new instance of the product and convert it to a floating point number:
phone = Product("phone", 999)
print(float(phone))  # 999.0
