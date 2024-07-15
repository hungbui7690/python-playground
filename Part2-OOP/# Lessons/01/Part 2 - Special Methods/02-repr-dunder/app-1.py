"""
Python __repr__
- The __repr__ dunder method defines behavior when you pass an instance of a class to the repr().

- The __repr__ method returns the string representation of an object. Typically, the __repr__() returns a string that can be executed and yield the same value as the object.

- In other words, if you pass the returned string of the object_name.__repr__() method to the eval() function, you’ll get the same value as the object_name. Let’s take a look at an example.


"""


# First, define the Person class with three instance attributes first_name, last_name, and age:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# Second, create a new instance of the Person class and display its string representation:
person = Person("John", "Doe", 25)
print(repr(person))  # <__main__.Person object at 0x000001B3F309F2D0>
