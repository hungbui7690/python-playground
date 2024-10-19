"""
Convert to a tuple or a dictionary

- The dataclasses module has the astuple() and asdict() functions that convert an instance of the dataclass to a tuple and a dictionary.

"""

# 1.
from dataclasses import dataclass, astuple, asdict


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100


p = Person("John Doe", 25)


# 2.
print(astuple(p))  # ('John Doe', 25, 100)
print(asdict(p))  # {'name': 'John Doe', 'age': 25, 'iq': 100}
