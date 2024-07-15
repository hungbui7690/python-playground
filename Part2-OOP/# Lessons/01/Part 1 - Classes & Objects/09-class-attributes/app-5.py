"""
3) Defining default values

Sometimes, you want to set a default value for all instances of a class. In this case, you can use a class attribute.

"""


# The following example defines a Product class. All the instances of the Product class will have a default discount specified by the default_discount class attribute:


class Product:
    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


p1 = Product(100)
print(p1.net_price())  # 100

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())  # 190


"""
Summary

- A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.

- Use class_name.class_attribute or object_name.class_attribute to access the value of the class_attribute.

- Use class attributes for storing class constant, track data across all instances, and setting default values for all instances of the class.

"""
