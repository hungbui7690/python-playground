"""
issubclass

- Everything is subclass of "object"
!! issubclass(Person, object)

"""


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title


# To check if a class is a subclass of another class, you use the issubclass() function. For example:
print(issubclass(Employee, Person))  # True


# The following defines the SalesEmployee class that inherits from the Employee class:
class SalesEmployee(Employee):
    pass


# The SalesEmployee is the subclass of the Employee class. It’s also a subclass of the Person class as shown in the following:
print(issubclass(SalesEmployee, Employee))  # True
print(issubclass(SalesEmployee, Person))  # True


# Note that when you define a class that doesn’t inherit from any class, it’ll implicitly inherit from the built-in object class.
# For example, the Person class inherits from the object class implicitly. Therefore, it is a subclass of the object class:
print(issubclass(Person, object))  # True


# In other words, all classes are subclasses of the object class.


"""
Summary

    Inheritance allows a class to reuse existing attributes and methods of another class.
    The class that inherits from another class is called a child class, a subclass, or a derived class.
    The class from which other classes inherit is call a parent class, a super class, or a base class.
    Use isinstance() to check if an object is an instance of a class.
    Use issubclass() to check if a class is a subclass of another class.
"""
