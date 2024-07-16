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


# The __get__ method
# Python calls the __get__ method of the Person‘s object when you access the first_name attribute. For example:
person = Person()

person.first_name = "John"
# __set__ was called with instance=<__main__.Person object at 0x000001B9B8001710> and value=John

print(person.first_name)
# __get__ was called with instance=<__main__.Person object at 0x000001B9B8001710> and owner=<class '__main__.Person'>
# John


# If the instance is not None, the __get__() method returns the value of the attribute with the name property_name of the instance object.
