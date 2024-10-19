"""
Create immutable objects

- To create readonly objects from a dataclass, you can set the frozen argument of the dataclass decorator to True

"""

from dataclasses import dataclass


# 1.
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    iq: int = 100


# 2. If you attempt to change the attributes of the object after it is created, you’ll get an error. For example:
p = Person("Jane Doe", 25)
# p.iq = 120  # dataclasses.FrozenInstanceError: cannot assign to field 'iq'
