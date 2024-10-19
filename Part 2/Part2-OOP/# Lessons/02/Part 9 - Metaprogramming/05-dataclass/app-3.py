"""
Default values


"""

from dataclasses import dataclass


# When using a regular class, you can define default values for attributes. For example, the following Person class has the iq parameter with the default value of 100.
class Person:
    def __init__(self, name, age, iq=100):
        self.name = name
        self.age = age
        self.iq = iq


# To define a default value for an attribute in the dataclass, you assign it to the attribute like this:
@dataclass
class PersonX:
    name: str
    age: int

    # Like the parameter rules, the attributes with the default values must appear after the ones without default values. If we move this line to the top, it won't work
    iq: int = 100


print(PersonX("John Doe", 25))  # PersonX(name='John Doe', age=25, iq=100)
