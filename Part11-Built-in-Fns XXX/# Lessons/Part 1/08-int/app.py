"""
int
- convert a number or a string to an integer.
- The int() accepts a string or a number and converts it to an integer. Here’s the int() constructor:

    int(x, base=10)

- Note that int() is a constructor of the built-in int class. It is not a function. When you call the int(), you create a new integer object.

- If x is a string, it should contain a number and is optionally preceded by an optional sign like a minus (-) or plus (+).
- If x is a floating point number, the int() returns the integer value of that number.
- If x is an object, the int() delegates to the x.__int()__ method. If the object x does not have the __int__() method, the int() will use the __index__() method.


- The x argument is optional. If you omit it, the int() will return 0

- The base specifies the base for the integer. It defaults to 10.

"""

# 1) Using the int() to convert a string to an integer
number = int("100")
print(number)  # 👉 100

number = int("-90")
print(number)  # 👉 -90

number = int(" -20\n")
print(number)  # 👉 -20


# 2) Using the int() to convert floating point numbers to integers
number = int(10.0)
print(number)  # 👉 10
number = int(9.99)
print(number)  # 👉 9
number = int(5.01)
print(number)  # 👉 5


# 3) Using the Python int() to convert an object to an integer
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # The __int__() method returns the integer of the age:
    def __int__(self):
        return int(self.age)


person = Person("John Doe", 22)
print(int(person))  # 👉 22
