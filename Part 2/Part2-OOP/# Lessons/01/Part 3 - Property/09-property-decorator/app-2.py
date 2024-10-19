"""
Property Decorator
- @property

    class property(fget=None, fset=None, fdel=None, doc=None)

"""


# To avoid this redundancy, you can rename the get_age() method to the age() method like this:
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def age(self):
        return self._age

    age = property(fget=age)


john = Person("John", 25)
print(john.age)  # 25
