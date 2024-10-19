"""
Python __bool__

"""


# An object of a custom class is associated with a boolean value. By default, it evaluates to True. For example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    person = Person("John", 25)
    print(bool(person))  # True


# In this example, we define the Person class, instantiate an object, and show its boolean value. As expected, the person object is True.
# To override this default behavior, you implement the __bool__ special method. The __bool__ method must return a boolean value, True or False.
