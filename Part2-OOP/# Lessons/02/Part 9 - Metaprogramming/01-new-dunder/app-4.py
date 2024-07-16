"""
When using the __new__ method


"""


# For example, the following defines the Person class and uses the __new__method to inject the full_name attribute to the Person’s object:
class Person:
    def __new__(cls, first_name, last_name):
        obj = super().__new__(cls)  # create a new object

        obj.first_name = first_name  # initialize attributes
        obj.last_name = last_name

        obj.full_name = f"{first_name} {last_name}"  # inject new attribute
        return obj


person = Person("John", "Doe")
print(person.full_name)  # John Doe

print(person.__dict__)
# {'first_name': 'John', 'last_name': 'Doe', 'full_name': 'John Doe'}


# Typically, when you override the __new__() method, you don’t need to define the __init__() method because everything you can do in the __init__() method, you can do it in the __new__() method.


# Summary
# The __new__() is a static method of the object class.
# When you create a new object by calling the class, Python calls the __new__() method to create the object first and then calls the __init__() method to initialize the object’s attributes.
# Override the __new__() method if you want to tweak the object at creation time.
