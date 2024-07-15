"""
Python __str__
- Internally, Python will call the __str__ method automatically when an instance calls the str() method.

- Note that the print() function converts all non-keyword arguments to strings by passing them to the str() before displaying the string values.

"""


# The following illustrates how to implement the __str__ method in the Person class:


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Person({self.first_name},{self.last_name},{self.age})"


# And when you use the print() function to print out an instance of the Person class, Python calls the __str__ method defined in the Person class. For example:
person = Person("John", "Doe", 25)
print(person)  # Person(John,Doe,25)


# Summary
# Implement the __str__ method to customize the string representation of an instance of a class.
