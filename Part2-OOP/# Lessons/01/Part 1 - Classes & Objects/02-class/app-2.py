"""
A class is also an object in Python

- Everything in Python is an object, including classes.

"""


class Person:
    pass


person = Person()


# When you define the Person class, Python creates an object with the name Person. The Person object has attributes. For example, you can find its name using the __name__ attribute:
print(Person.__name__)  # Person


# The Person object has the type of type:
print(type(Person))  # <class 'type'>


# The Person class also has a behavior. For example, it can create a new instance:
person = Person()


# Summary
# An object is container that contains state and behavior.
# A class is a blueprint for creating objects.
# In Python, a class is also an object, which is an instance of the type.
