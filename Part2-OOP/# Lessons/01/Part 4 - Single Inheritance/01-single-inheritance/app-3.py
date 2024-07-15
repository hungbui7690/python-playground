"""
type vs. isinstance

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


# The following shows the type of instances of the Person and Employee classes:
person = Person("Jane")
print(type(person))  # <class '__main__.Person'>

employee = Employee("John", "Python Developer")
print(type(employee))  # <class '__main__.Employee'>


# To check if an object is an instance of a class, you use the isinstance() method. For example:
print(isinstance(person, Person))  # True

print(isinstance(employee, Person))  # True
print(isinstance(employee, Employee))  # True
print(isinstance(person, Employee))  # False


"""
As clearly shown in the output:

    The person is an instance of the Person class.
    The employee is an instance of the Employee class. It’s also an instance of the Person class.
    The person is not an instance of the Employee class.

In practice, you’ll often use the isinstance() function to check whether an object has certain methods. Then, you’ll call the methods of that object.

"""
