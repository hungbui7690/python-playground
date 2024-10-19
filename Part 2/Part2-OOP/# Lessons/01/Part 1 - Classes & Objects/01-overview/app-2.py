"""
Define instance attributes

"""


class Person:
    pass


person = Person()


# Define instance attributes

# Python is dynamic. It means that you can add an attribute to an instance of a class dynamically at runtime.
# For example, the following adds the name attribute to the person object:
person.name = "John"
# However, if you create another Person object, the new object won’t have the name attribute.
