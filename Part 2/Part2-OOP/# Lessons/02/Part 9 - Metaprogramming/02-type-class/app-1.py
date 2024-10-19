"""
Python type Class


"""


# In Python, a class is an object of the class type. For example, the following defines the Person class with two methods __init__ and greeting:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, I am {self.name}. I am {self.age} year old."


print(type(Person))  # <class 'type'>
print(isinstance(Person, type))  # True
