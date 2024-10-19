"""
Python Property
- use it to define properties for a class.

"""


# The following defines a Person class that has two attributes name and age, and create a new instance of the Person class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 18)


# Since age is the instance attribute of the Person class, you can assign it a new value like this:
john.age = 19


# The following assignment is also technically valid:
john.age = -1


# However, the age is semantically incorrect.
# To ensure that the age is not zero or negative, you use the if statement to add a check as follows:
age = -1
if age <= 0:
    raise ValueError("The age must be positive")
else:
    john.age = age


# And you need to do this every time you want to assign a value to the age attribute. This is repetitive and difficult to maintain.
# To avoid this repetition, you can define a pair of methods called getter and setter.
