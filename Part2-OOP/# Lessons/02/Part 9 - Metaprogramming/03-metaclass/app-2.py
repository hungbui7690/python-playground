"""
Metaclass


"""

from pprint import pprint


# First, define a custom metaclass called Human that has the freedom attribute sets to True by default:
class Human(type):
    # Note that the __new__ method returns a new class or a class object.
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_


# Second, define the Person class that uses the Human metaclass:
class Person(object, metaclass=Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# The Person class will have the freedom attribute as shown in the class variables:
pprint(Person.__dict__)

"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__init__': <function Person.__init__ at 0x00000248D4545940>,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'freedom': True})
"""
