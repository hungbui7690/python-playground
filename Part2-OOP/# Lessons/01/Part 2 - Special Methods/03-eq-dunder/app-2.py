"""
Python __eq__

"""


# Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class. By default, Python uses the is operator if you don’t provide a specific implementation for the __eq__ method.


# The following shows how to implement the __eq__ method in the Person class that returns True if two person objects have the same age:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Check the age of 2 instances
    def __eq__(self, other):
        return self.age == other.age


john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)
mary = Person("Mary", "Doe", 27)

print(john == jane)  # True
print(john == mary)  # False


# The following compares a Person object with an integer:
print(john == 20)
# AttributeError: 'int' object has no attribute 'age'
