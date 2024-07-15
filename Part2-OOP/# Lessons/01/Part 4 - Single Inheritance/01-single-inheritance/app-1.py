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


# The Person class has the name attribute and the greet() method.
# Now, you want to define the Employee that is similar to the Person class:
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def greet(self):
        return f"Hi, it's {self.name}"


# The Employee class has two attributes name and job_title. It also has the greet() method that is exactly the same as the greet() method of the Person class.
# To reuse the greet() method from the Person class in the Employee class, you can create a relationship between the Person and Employee classes. To do it, you use inheritance so that the Employee class inherits from the Person class.
