"""
Metaclass Parameters

- To pass parameters to a metaclass, you use the keyword arguments.

"""

from pprint import pprint


# For example, the following redefines the Human metaclass that accepts keyword arguments, where each argument becomes a class variable:
class Human(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_


# The following uses the Human metaclass to create a Person class with the country and freedom class variables set to USA and True respectively:
class Person(object, metaclass=Human, country="USA", freedom=True):
    def __init__(self, name, age):
        self.name = name
        self.age = age


pprint(Person.__dict__)
"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__doc__': None,
            '__init__': <function Person.__init__ at 0x0000015287CD5940>,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'country': 'USA',
            'freedom': True})
"""


"""
When to use metaclasses

    Here’s the quote from Tim Peter who wrote the Zen of Python:

        Metaclasses are deeper magic that 99% of users should never worry about it. If you wonder whether you need them, you don’t (the people who actually need them to know with certainty that they need them and don’t need an explanation about why).
        Tim Peter

    In practice, you often don’t need to use metaclasses unless you maintain or develop the core of large frameworks such as Django.

\\\\\\\\\\\\\\\\

Summary
- A metaclass is a class that creates other classes.

"""
