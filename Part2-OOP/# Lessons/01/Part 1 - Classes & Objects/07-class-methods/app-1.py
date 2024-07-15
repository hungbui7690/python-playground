"""
Class Methods
- So far, you learned about instance methods that are bound to a specific instance of a class.

- Instance methods can access instance variables within the same class. To invoke instance methods, you need to create an instance of the class first.

"""


# The following defines the Person class:


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."


# The Person class has three instance methods including __init__(), get_full_name(), and introduce().
# Suppose that you want to add a method that creates an anonymous person to the Person class.


# In order to do so, you would come up with the following code:
class PersonX:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def create_anonymous(self):
        return Person("John", "Doe", 25)


joe = PersonX("Joe", "Doe", 20)
john = joe.create_anonymous()
print(john.first_name)  # John

# The create_anonymous() is an instance method that returns an anonymous person.
# However, to invoke the create_anonymous() method, you need to create an instance, which doesn’t make sense in this case.
# This is why Python class methods come into play.
