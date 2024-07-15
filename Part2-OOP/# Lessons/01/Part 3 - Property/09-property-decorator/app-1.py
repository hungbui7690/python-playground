"""
Property Decorator
- @property

    class property(fget=None, fset=None, fdel=None, doc=None)

"""


# The following defines a Person class with two attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    # To define a getter for the age attribute, you use the property class like this:
    def get_age(self):
        return self._age

    age = property(fget=get_age)


# The following creates an instance of the Person class and get the value of the age property via the instance:
john = Person("John", 25)
print(john.age)  # 25


# Also, you can call the get_age() method of the Person object directly like this:
print(john.get_age())  # 25

# So to get the age of a Person object, you can use either the age property or the get_age() method. This creates an unnecessary redundancy.
