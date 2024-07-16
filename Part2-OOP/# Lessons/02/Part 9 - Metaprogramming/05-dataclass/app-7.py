"""
Sort objects
- By default, a dataclass implements the __eq__ method.
- To allow different types of comparisons like __lt__, __lte__, __gt__, __gte__, you can set the order argument of the @dataclass decorator to True:

    @dataclass(order=True)

- By doing this, the dataclass will sort the objects by every field until it finds a value that’s not equal.
- In practice, you often want to compare objects by a particular attribute, not all attributes. To do that, you need to define a field called sort_index and set its value to the attribute that you want to sort.
- For example, suppose you have a list of Person‘s objects and want to sort them by age:

    members = [
        Person('John', 25),
        Person('Bob', 35),
        Person('Alice', 30)
    ]

- To do that, you need to:

    First, pass the order=True parameter to the @dataclass decorator.
    Second, define the sort_index attribute and set its init parameter to False.
    Third, set the sort_index to the age attribute in the __post_init__ method to sort the Person‘s object by age.

"""

# The following shows the code for sorting Person‘s objects by age:
from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        # sort by age
        self.sort_index = self.age


members = [
    Person(name="John", age=25),
    Person(name="Bob", age=35),
    Person(name="Alice", age=30),
]

sorted_members = sorted(members)

for member in sorted_members:
    print(f"{member.name}(age={member.age})")
# John(age=25)
# Alice(age=30)
# Bob(age=35)


"""
Summary

    Use the @dataclass decorator from the dataclasses module to make a class a dataclass. The dataclass object implements the __eq__ and __str__ by default.
    Use the astuple() and asdict() functions to convert an object of a dataclass to a tuple and dictionary.
    Use frozen=True to define a class whose objects are immutable.
    Use __post_init__ method to initialize attributes that depends on other attributes.
    Use sort_index to specify the sort attributes of the dataclass objects.
"""
