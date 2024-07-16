"""
HOW DESCRIPTORS WORK


"""

from pprint import pprint


# The following modifies the RequiredString class to include the print statements that print out the arguments.
class RequiredString:
    def __set_name__(self, owner, name):
        print(f"__set_name__ was called with owner={owner} and name={name}")
        self.property_name = name

    def __get__(self, instance, owner):
        print(f"__get__ was called with instance={instance} and owner={owner}")
        if instance is None:
            return self

        return instance.__dict__[self.property_name] or None

    def __set__(self, instance, value):
        print(f"__set__ was called with instance={instance} and value={value}")

        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must a string")

        if len(value) == 0:
            raise ValueError(f"The {self.property_name} cannot be empty")

        instance.__dict__[self.property_name] = value


class Person:
    first_name = RequiredString()
    last_name = RequiredString()


# The __set__ method
# When you assign the new value to a descriptor, Python calls __set__ method to set the attribute on an instance of the owner class to the new value. For example:
person = Person()
person.first_name = "Alex"
# __set__ was called with instance=<__main__.Person object at 0x0000012845BB15D0> and value=Alex

"""
- Otherwise, we assign the value to the instance attribute first_name of the person object:

    instance.__dict__[self.property_name] = value

- Note that Python uses instance.__dict__ dictionary to store instance attributes of the instance object.

- Once you set the first_name and last_name of an instance of the Person object, you’ll see the instance attributes with the same names in the instance’s __dict__. For example:
"""
personX = Person()
print(personX.__dict__)  # {}

personX.first_name = "John"
personX.last_name = "Doe"
# __set__ was called with instance=<__main__.Person object at 0x0000020831BF9890> and value=John
# __set__ was called with instance=<__main__.Person object at 0x0000020831BF9890> and value=Doe

print(personX.__dict__)  # {'first_name': 'John', 'last_name': 'Doe'}
