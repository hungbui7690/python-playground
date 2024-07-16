"""
Define a metaclass

"""


# First, define the Data metaclass that inherits from the type class:
# Second, override the __new__ method to return a new class object:
class Data(type):
    def __new__(mcs, name, bases, class_dict):
        class_obj = super().__new__(mcs, name, bases, class_dict)
        return class_obj


# Note that the __new__ method is a static method of the Data metaclass. And you don’t need to use the @staticmethod decorator because Python treats it special.
# Also, the __new__ method creates a new class like the Person class, not the instance of the Person class.
