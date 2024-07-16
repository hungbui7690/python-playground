"""
Python None
- In Python, None is a special object of the NoneType class. To use the None value, you specify the None as follows:

    None

"""

# If you use the type() function to check the type of the None value, you’ll get NoneType class:
print(type(None))  # <class 'NoneType'>
# The None is a singleton object of the NoneType class. It means that Python creates one and only one None object at runtime.


# Therefore, if you use the equality (==) or is operator to compare None with None, you’ll get the result of True:
print(None == None)  # True
print(None is None)  # True
# It’s a good practice to use the is or is not operator to compare a value with None.


# The reason is that the user-defined objects may change the equality operator’s behavior by overriding the __eq__() method. For example:
class Apple:
    def __eq__(self, other):
        return True


apple = Apple()
print(apple == None)  # True

"""
Note that you cannot override the is operator behavior like you do with the equality operator (==).

It’s also important to note that the None object has the following features:

    None is not zero (0, 0.0, …).
    None is not the same as False.
    None is not the same as an empty string ('').
    Comparing None to any value will return False except None itself.
"""
