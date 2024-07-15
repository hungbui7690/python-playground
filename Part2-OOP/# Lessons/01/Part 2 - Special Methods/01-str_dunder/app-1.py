"""
Python __str__

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# The Person class has three instance attributes including first_name, last_name, and age.
# The following creates a new instance of the Person class and display it:
person = Person("John", "Doe", 25)
print(person)  # <__main__.Person object at 0x00000279263AF310>


"""
When you use the print() function to display the instance of the Person class, the print() function shows the memory address of that instance.

Sometimes, it’s useful to have a string representation of an instance of a class. To customize the string representation of a class instance, the class needs to implement the __str__ magic method.
"""
