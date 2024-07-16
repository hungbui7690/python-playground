"""
Metaclass Example

"""


# The following defines a Person class with two attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(f"{self.name, self.age}")

    def __str__(self):
        return f"Person(name={self.name},age={self.age})"

    def __repr__(self):
        return f"Person(name={self.name},age={self.age})"


"""
Typically, when defining a new class, you need to:

    - Define a list of object’s properties.
    - Define an __init__ method to initialize object’s attributes.
    - Implement the __str__ and __repr__ methods to represent the objects in human-readable and machine-readable formats.
    - Implement the __eq__ method to compare objects by values of all properties.
    - Implement the __hash__ method to use the objects of the class as keys of a dictionary or elements of a set.

As you can see, it requires a lot of code.


Imagine you want to define a Person class like this and automatically has all the functions above:

    class Person:
        props = ['first_name', 'last_name', 'age']

To do that, you can use a metaclass.

"""
