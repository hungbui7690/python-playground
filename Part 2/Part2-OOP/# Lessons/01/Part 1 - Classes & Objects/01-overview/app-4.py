"""
Define instance methods


"""


# The following adds an instance method called greet() to the Person class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."


# To call an instance method, you also use the dot notation. For example:
person = Person("John", 25)
print(person.greet())  # Hi, it's John.
