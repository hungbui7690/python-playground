"""
Metaclass
- A metaclass is a class that creates other classes. By default, Python uses the type metaclass to create other classes.

"""


# For example, the following defines a Person class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# When Python executes the code, it uses the type metaclass to create the Person class. The reason is that the Person class uses the type metaclass by default.
# The explicit Person class definition looks like this:
class PersonX(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# The metaclass argument allows you to specify which metaclass class to use to define the class. Therefore, you can create a custom metaclass that has its own logic to create other classes. By using a custom metaclass, you can inject functionality into the class creation process.
