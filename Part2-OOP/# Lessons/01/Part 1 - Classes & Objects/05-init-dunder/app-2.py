"""
The __init__ method with default parameters

"""


# The __init__() method’s parameters can have default values. For example:


class Person:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


if __name__ == "__main__":
    person = Person("John")
    print(f"I'm {person.name}. I'm {person.age} years old.")


# In this example, the age parameter has a default value of 22. Because we don’t pass an argument to the Person(), the age uses the default value.


# Summary
# Use the __init__() method to initialize the object’s attributes.
# The __init__() doesn’t create an object but is automatically called after the object is created.
