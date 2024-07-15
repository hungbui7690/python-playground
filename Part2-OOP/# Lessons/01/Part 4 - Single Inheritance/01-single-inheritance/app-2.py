"""
Inheritance
- Inheritance allows a class to reuse the logic of an existing class

"""


# Suppose you have the following Person class:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


# The following redefines the Employee class that inherits from the Person class:
class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title


# By doing this, the Employee class behaves the same as the Person class without redefining the greet() method.
# This is a single inheritance because the Employee inherits from a single class (Person). Note that Python also supports multiple inheritances where a class inherits from multiple classes.
# Since the Employee inherits attributes and methods of the Person class, you can use the instance of the Employee class as if it were an instance of the Person class.


# For example, the following creates a new instance of the Employee class and call the greet() method:
employee = Employee("John", "Python Developer")
print(employee.greet())  # Hi, it's John


"""
Inheritance terminology

- The Person class is the parent class, the base class, or the super class of the Employee class. And the Employee class is a child class, a derived class, or a subclass of the Person class.

- The Employee class derives from, extends, or subclasses the Person class.

- The relationship between the Employee class and Person class is IS-A relationship. In other words, an employee is a person.

"""
