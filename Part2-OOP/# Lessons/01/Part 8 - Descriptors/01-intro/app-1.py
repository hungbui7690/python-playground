"""
Descriptors


"""


# Suppose you have a class Person with two instance attributes first_name and last_name:
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


# And you want the first_name and last_name attributes to be non-empty strings. These plain attributes cannot guarantee this.
# To enforce the data validity, you can use property with a getter and setter methods, like this:
class PersonX:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("The first name must a string")

        if len(value) == 0:
            raise ValueError("The first name cannot be empty")

        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("The last name must a string")

        if len(value) == 0:
            raise ValueError("The last name cannot be empty")

        self._last_name = value


"""
In this Person class, the getter returns the attribute value while the setter validates it before assigning it to the attribute.

This code works perfectly fine. However, it is redundant because the validation logic validates the first and last names is the same.

Also, if the class has more attributes that require a non-empty string, you need to duplicate this logic in other properties. In other words, this validation logic is not reusable.

To avoid duplicating the logic, you may have a method that validates data and reuse this method in other properties. This approach will enable reusability. However, Python has a better way to solve this by using descriptors.

"""
