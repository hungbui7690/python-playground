"""
Python __repr__
- __repr__ methods effects the print function

- After setup the __repr__ method, we can use these 2 functions to call it
!! print(repr(person))
!! print(person)

"""


# By default, the output contains the memory address of the person object. To customize the string representation of the object, you can implement the __repr__ method like this:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'


# When you pass an instance of the Person class to the repr(), Python will call the __repr__ method automatically. For example:
person = Person("John", "Doe", 25)
print(repr(person))  # Person("John","Doe",25)
print(person)  # Person("John","Doe",25)
