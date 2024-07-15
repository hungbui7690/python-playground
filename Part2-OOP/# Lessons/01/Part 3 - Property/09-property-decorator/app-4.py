"""
Setter decorators

"""


# The following adds a setter method (set_age) to assign a value to _age attribute to the Person class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value


# To assign the set_age to the fset of the age property object, you call the setter() method of the age property object like the following:
class PersonX:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

    age = age.setter(set_age)


# The setter() method accepts a callable and returns another callable (a property object). Therefore, you can use the decorator @age.setter for the set_age() method like this:
class PersonY:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value


# Now, you can change the set_age() method to the age() method and use the age property in the __init__() method:
class PersonZ:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value


# To summarize, you can use decorators to create a property using the following pattern:
class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value


# In this pattern, the __attr is the private attribute and prop is the property name.


# The following example uses the @property decorators to create the name and age properties in the Person class:
class PersonV:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("The name cannot be empty")
        self._name = value
