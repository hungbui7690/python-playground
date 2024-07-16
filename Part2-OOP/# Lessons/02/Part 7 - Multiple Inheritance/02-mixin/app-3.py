"""
Compose multiple mixin classes


"""

from pprint import pprint
import json


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


class Person:
    def __init__(self, name):
        self.name = name


# Suppose you want to convert the Employee‘s object to JSON. To do that, you can first define a new mixin class that use the json standard module:
class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


# And then change the Employee class so that it inherits the JSONMixin class:
class Employee(DictMixin, JSONMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


# The following creates a new instance of the Employee class and converts it to a dictionary and json:
if __name__ == "__main__":
    e = Employee(
        name="John",
        skills=["Python Programming" "Project Management"],
        dependents={"wife": "Jane", "children": ["Alice", "Bob"]},
    )

    pprint(e.to_dict())
    print(e.to_json())

"""
{'dependents': {'children': ['Alice', 'Bob'], 'wife': 'Jane'},
'name': 'John',
'skills': ['Python ProgrammingProject Management']}

{"name": "John", "skills": ["Python ProgrammingProject Management"], "dependents": {"wife": "Jane", "children": ["Alice", "Bob"]}}
"""


# Summary
# A mixin class provides method implementations for reuse by multiple related subclasses.
