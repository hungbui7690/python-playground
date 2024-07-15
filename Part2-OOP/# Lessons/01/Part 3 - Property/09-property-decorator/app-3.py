"""
Property Decorator
- @property

    class property(fget=None, fset=None, fdel=None, doc=None)

"""


# The property() accepts a callable (age) and returns a callable. Therefore, it is a decorator. Therefore, you can use the @property decorator to decorate the age() method as follows:
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age


# So by using the @property decorator, you can simplify the property definition for a class.
john = Person("John", 25)
print(john.age)  # 25
