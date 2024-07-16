"""
Define __repr__ method

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

        # define __init__
        setattr(class_obj, "__init__", Data.init(class_obj))

        # 1. define __repr__
        setattr(class_obj, "__repr__", Data.repr(class_obj))

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

    # 2.
    @staticmethod
    def repr(class_obj):
        def _repr(self):
            prop_values = (getattr(self, prop) for prop in class_obj.props)
            prop_key_values = (
                f"{key}={value}" for key, value in zip(class_obj.props, prop_values)
            )
            prop_key_values_str = ", ".join(prop_key_values)
            return f"{class_obj.__name__}({prop_key_values_str})"

        return _repr


class Person(metaclass=Data):
    props = ["name", "age"]


p = Person("John Doe", age=25)
print(p)  # Person(name=John Doe, age=25)
