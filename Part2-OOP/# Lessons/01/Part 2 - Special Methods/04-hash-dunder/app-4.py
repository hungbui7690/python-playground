"""
Python __hash__


"""


# To make the Person work well in data structures like dictionaries, the hash of the class should remain immutable. To do it, you can make the age attribute of the Person class a read-only property:


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


print(hash(Person("John", 22)))


# Summary
# By default, __hash__ uses the id of objects and __eq__ uses the is operator for comparisons.
# If you implement __eq__, Python sets __hash__ to None unless you implement __hash__.
