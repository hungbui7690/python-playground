"""
Python __hash__
- By default, the __hash__ uses the object’s identity and the __eq__ returns True if two objects are the same. To override this default behavior, you can implement the __eq__ and __hash__.

- If a class overrides the __eq__ method, the objects of the class become unhashable. This means that you won’t able to use the objects in a mapping type. For example, you will not able to use them as keys in a dictionary or elements in a set.

"""


# The following Person class implements the __eq__ method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age


# If you attempt to use the Person object in a set, you’ll get an error. For example:
members = {Person("John", 22), Person("Jane", 22)}
# TypeError: unhashable type: 'Person'


# Also, the Person’s object loses hashing because if you implement __eq__, the __hash__ is set to None. For example:
hash(Person("John", 22))
