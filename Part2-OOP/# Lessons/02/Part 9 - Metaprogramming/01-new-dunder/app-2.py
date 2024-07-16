"""
Python __new__


"""


# The following illustrates the sequence which Python calls the __new__ and __init__ method when you create a new object by calling the class:
class Person:
    def __new__(cls, name):
        print(f"Creating a new {cls.__name__} object...")
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print("Initializing the person object...")
        self.name = name


person = Person("John")
# Creating a new Person object...
# Initializing the person object...
