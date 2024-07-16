"""
Decorator

"""


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
        Data.define_property(class_obj)

        setattr(class_obj, "__init__", Data.init(class_obj))
        setattr(class_obj, "__repr__", Data.repr(class_obj))
        setattr(class_obj, "__eq__", Data.eq(class_obj))
        setattr(class_obj, "__hash__", Data.hash(class_obj))

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

    @staticmethod
    def eq(class_obj):
        def _eq(self, other):
            if not isinstance(other, class_obj):
                return False

            self_values = [getattr(self, prop) for prop in class_obj.props]
            other_values = [getattr(other, prop) for prop in other.props]

            return self_values == other_values

        return _eq

    @staticmethod
    def hash(class_obj):
        def _hash(self):
            values = (getattr(self, prop) for prop in class_obj.props)
            return hash(tuple(values))

        return _hash


class Person(metaclass=Data):
    props = ["name", "age"]


# 1.
class Employee(metaclass=Data):
    props = ["name", "job_title"]


# 2.
if __name__ == "__main__":
    e = Employee(name="John Doe", job_title="Python Developer")
    print(e)  # Employee(name=John Doe, job_title=Python Developer)


# It works as expected. However, specifying the metaclass is quite verbose. To improve this, you can use a function decorator.
