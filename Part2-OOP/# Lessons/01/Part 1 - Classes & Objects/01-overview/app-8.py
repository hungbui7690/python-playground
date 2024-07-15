"""
Single inheritance

- A class can reuse another class by inheriting it. When a child class inherits from a parent class, the child class can access the attributes and methods of the parent class.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."


"""
- Inside the __init__ method of the Employee class calls the __init__method of the Person class to initialize the name and age attributes. The super() allows a child class to access a method of the parent class.
- The Employee class extends the Person class by adding one more attribute called job_title
- The Person is the parent class while the Employee is a child class. To override the greet() method in the Person class, you can define the greet() method in the Employee class as follows:
"""


# For example, you can define an Employee class that inherits from the Person class:
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."


# The greet() method in the Employee is also called the greet() method of the Person class. In other words, it delegates to a method of the parent class.
# The following creates a new instance of the Employee class and call the greet() method:
employee = Employee("John", 25, "Python Developer")
print(employee.greet())  # Hi, it's John. I'm a Python Developer.
