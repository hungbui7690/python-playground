"""
Define class attributes
- Unlike instance attributes, class attributes are shared by all instances of the class. They are helpful if you want to define class constants or variables that keep track of the number of instances of a class.


"""


# For example, the following defines the counter class attribute in the Person class:
class Person:
    counter = 0  # (1)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1  # (2)

    def greet(self):
        return f"Hi, it's {self.name}."


# You can access the counter attribute from the Person class:
print(Person.counter)  # 0


# Or from any instances of the Person class:
person = Person("John", 25)
person = Person("Jane", 18)
print(person.counter)  # 2
