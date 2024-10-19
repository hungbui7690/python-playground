"""
Customize attribute behaviors

- If don’t want to initialize an attribute in the __init__ method, you can use the field() function from the dataclasses module.

- The field() function has multiple interesting parameters such as repr, hash, compare, and metadata.

- If you want to initialize an attribute that depends on the value of another attribute, you can use the __post_init__ method. As its name implies, Python calls the __post_init__ method after the __init__ method.

"""

from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    # The following use the __post_init__ method to initialize the can_vote attribute based on the age attribute:
    def __post_init__(self):
        print("called __post_init__ method")
        self.can_vote = 18 <= self.age <= 70


p = Person("Jane Doe", 25)
print(p)
# called __post_init__ method
# Person(name='Jane Doe', age=25, iq=100, can_vote=True)
