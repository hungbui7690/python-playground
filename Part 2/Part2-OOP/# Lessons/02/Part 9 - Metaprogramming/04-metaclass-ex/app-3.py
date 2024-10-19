"""
Create property objects

"""

from pprint import pprint


# First, define a Prop class that accepts an attribute name and contains three methods for creating a property object(set, get, and delete). The Data metaclass will use this Prop class for adding property objects to the class.
class Prop:
    def __init__(self, attr):
        self._attr = attr

    def get(self, obj):
        return getattr(obj, self._attr)

    def set(self, obj, value):
        return setattr(obj, self._attr, value)

    def delete(self, obj):
        return delattr(obj, self._attr)


# Second, create a new static method define_property() that creates a property object for each attribute from the props list:
class Data(type):
    def __new__(mcs, name, bases, class_dict):
        class_obj = super().__new__(mcs, name, bases, class_dict)
        Data.define_property(class_obj)

        return class_obj

    @staticmethod
    def define_property(class_obj):
        for prop in class_obj.props:
            attr = f"_{prop}"
            prop_obj = property(
                fget=Prop(attr).get, fset=Prop(attr).set, fdel=Prop(attr).delete
            )
            setattr(class_obj, prop, prop_obj)

        return class_obj


# The following defines the Person class that uses the Data metaclass:
class Person(metaclass=Data):
    props = ["name", "age"]


# The Person class has two properties name and age:
pprint(Person.__dict__)

"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
            '__doc__': None,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            'age': <property object at 0x0000024EFDFE9210>,
            'name': <property object at 0x0000024EFDFE9120>,
            'props': ['name', 'age']})
"""

# It has "name", "age", and "props"
