"""
Python __eq__

"""


# Suppose that you have the following Person class with three instance attributes: first_name, last_name, and age:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# And you create two instances of the Person class:
john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)


# In this example, the john and jane objects are not the same object. And you can check it using the is operator:
print(john is jane)  # False


# Also, when you compare john with jane using the equal operator (==), you’ll get the result of False:
print(john == jane)  # False


"""
Since john and jane have the same age, you want them to be equal. In other words, you want the following expression to return True:

    john == jane

To do it, you can implement the __eq__ dunder method in the Person class.

"""
