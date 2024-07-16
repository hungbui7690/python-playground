"""
Python dataclass
- Python introduced the dataclass in version 3.7 (PEP 557). The dataclass allows you to define classes with less code and more functionality out of the box.

"""


# The following defines a regular Person class with two instance attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
This Person class has the __init__ method that initializes the name and age attributes.

If you want to have a string representation of the Person object, you need to implement the __str__ or __repr__ method. Also, if you want to compare two instances of the Person class by an attribute, you need to implement the __eq__ method.

However, if you use the dataclass, you’ll have all of these features (and even more) without implementing these dunder methods.
"""
