"""
Python __repr__
- if we have both __repr__ and __str__ methods setup:
    + if we call print(), it will run the __str__
    + if we call print(repr()), it will run the __repr__

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f"({self.first_name},{self.last_name},{self.age})"


person = Person("John", "Doe", 25)

# use str()
print(person)  # (John,Doe,25)

# use repr()
print(repr(person))  # Person("John","Doe",25)


# When a class doesn’t implement the __str__ method and you pass an instance of that class to the str(), Python returns the result of the __repr__ method because internally the __str__ method calls the __repr__ method.


"""
__str__ vs __repr__

- The main difference between __str__ and __repr__ method is intended audiences.

- The __str__ method returns a string representation of an object that is human-readable 
- while the __repr__ method returns a string representation of an object that is machine-readable.

\\\\\\\\\\\\\

Summary

- Implement the __repr__ method to customize the string representation of an object when repr() is called on it.
- The __str__ calls __repr__ internally by default.

"""
