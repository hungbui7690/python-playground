"""
Define __init__ method

"""

from pprint import pprint


class Prop:
    def __init__(self, attr):
        self._attr = attr

    def get(self, obj):
        return getattr(obj, self._attr)

    def set(self, obj, value):
        return setattr(obj, self._attr, value)

    def delete(self, obj):
        return delattr(obj, self._attr)


class Data(type):
    def __new__(mcs, name, bases, class_dict):
        class_obj = super().__new__(mcs, name, bases, class_dict)
        Data.define_property(class_obj)  # create property

        # 1. define __init__
        setattr(class_obj, "__init__", Data.init(class_obj))

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

    # 2.
    @staticmethod
    def init(class_obj):
        def _init(self, *obj_args, **obj_kwargs):
            if obj_kwargs:
                for prop in class_obj.props:
                    if prop in obj_kwargs.keys():
                        setattr(self, prop, obj_kwargs[prop])

            if obj_args:
                for kv in zip(class_obj.props, obj_args):
                    setattr(self, kv[0], kv[1])

        return _init


class Person(metaclass=Data):
    props = ["name", "age"]


# The p.__dict__ contains two attributes _name and _age based on the predefined names in the props list.
p = Person("John Doe", age=25)
pprint(p.__dict__)  # {'_age': 25, '_name': 'John Doe'}
