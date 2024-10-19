"""
Define and initialize an attribute

@@ def __init__(self, name, age):

"""


# To define and initialize an attribute for all instances of a class, you use the __init__ method. The following defines the Person class with two instance attributes name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# When you create a Person object, Python automatically calls the __init__ method to initialize the instance attributes. In the __init__ method, the self is the instance of the Person class.
# The following creates a Person object named person:
person = Person("John", 25)


# The person object now has the name and age attributes. To access an instance attribute, you use the dot notation. For example, the following returns the value of the name attribute of the person object:
print(person.name)  # John
print(person.age)  # 25
