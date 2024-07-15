"""
Getter and setter

- The getter and setter methods provide an interface for accessing an instance attribute:

    The getter returns the value of an attribute
    The setter sets a new value for an attribute

- In our example, you can make the age attribute private (by convention) and define a getter and a setter to manipulate the age attribute.

"""


# The following shows the new Person class with a getter and setter for the age attribute:
# In the Person class, the set_age() is the setter and the get_age() is the getter. By convention the getter and setter have the following name: get_<attribute>() and set_<attribute>().
class Person:
    # In the __init__() method, we call the set_age() setter method to initialize the _age attribute:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    # In the set_age() method, we raise a ValueError if the age is less than or equal to zero. Otherwise, we assign the age argument to the _age attribute:
    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    # The get_age() method returns the value of the _age attribute:
    def get_age(self):
        return self._age


# The following attempts to assign an invalid value to the age attribute:
john = Person("John", 18)
# john.set_age(-19) # ValueError: The age must be positive


# This code works just fine. But it has a backward compatibility issue.
# Suppose you released the Person class for a while and other developers have been already using it. And now you add the getter and setter, all the code that uses the Person won’t work anymore.
# To define a getter and setter method while achieving backward compatibility, you can use the property() class.
