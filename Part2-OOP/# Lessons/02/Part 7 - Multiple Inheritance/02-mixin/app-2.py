"""
What is a mixin in Python


"""

from pprint import pprint


# However, you may want to convert objects of other classes to dictionaries. To make the code reusable, you can define a mixin class called DictMixin like the following:
class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


"""
The DictMixin class has the to_dict() method that converts an object to a dictionary.

The _traverse_dict() method iterates the object’s attributes and assigns the key and value to the result.

The attribute of an object may be a list, a dictionary, or an object with the __dict__ attribute. Therefore, the _traverse_dict() method uses the _traverse() method to convert the attribute to value.
"""


class Person:
    def __init__(self, name):
        self.name = name


# To convert instances of the Employee class to dictionaries, the Employee needs to inherit from both DictMixin and Person classes:
class Employee(DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


# Note that you need to specify the mixin classes before other classes.
# The following creates a new instance of the Employee class and converts it to a dictionary:
e = Employee(
    name="John",
    skills=["Python Programming", "Project Management"],
    dependents={"wife": "Jane", "children": ["Alice", "Bob"]},
)

pprint(e.to_dict())
"""
{'dependents': {'children': ['Alice', 'Bob'], 'wife': 'Jane'},
'name': 'John',
'skills': ['Python Programming', 'Project Management']}
"""
