"""
Descriptors


"""


# First, define a descriptor class that implements three methods __set_name__, __get__, and __set__:
class RequiredString:
    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must be a string")

        if len(value) == 0:
            raise ValueError(f"The {self.property_name} cannot be empty")

        instance.__dict__[self.property_name] = value


# Second, use the RequiredString class in the Person class:
class Person:
    first_name = RequiredString()
    last_name = RequiredString()


# If you assign an empty string or a non-string value to the first_name or last_name attribute of the Person class, you’ll get an error.
# For example, the following attempts to assign an empty string to the first_name attribute:
try:
    person = Person()
    person.first_name = ""
except ValueError as e:
    print(e)
# Error: The first_name must be a string
"""
Also, you can use the RequiredString class in any class with attributes that require a non-empty string value.

Besides the RequiredString, you can define other descriptors to enforce other data types like age, email, and phone. And this is just a simple application of the descriptors.

Let’s understand how descriptors work.


"""
