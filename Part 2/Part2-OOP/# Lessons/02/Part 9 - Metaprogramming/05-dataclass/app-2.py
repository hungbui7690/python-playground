"""
Python dataclass


"""

# First, import the dataclass decorator from the dataclasses module:
from dataclasses import dataclass


# Second, decorate the Person class with the dataclass decorator and declare the attributes:
@dataclass
class Person:
    name: str
    age: int


"""
In this example, the Person class has two attributes name with the type str and age with the type int. By doing this, the @dataclass decorator implicitly creates the __init__ method like this:

    def __init__(name: str, age: int)

Note that the order of the attributes declared in the class will determine the orders of the parameters in the __init__ method.
"""


p1 = Person("John", 25)
p2 = Person("John", 25)


# When printing out the Person‘s object, you’ll get a readable format:
print(p1)  # Person(name='John', age=25)


# Also, if you compare two Person‘s objects with the same attribute value, it’ll return True. For example:
print(p1 == p2)  # True
