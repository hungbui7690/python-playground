"""
Python Type Hints
- how to use the mypy tool to check types statically.


Introduction to Python type hints

- Some programming languages have static typing, such as C/C++. It means you need to declare types of variables, parameters, and return values of a function upfront. The predefined types allow the compilers to check the code before compiling and running the program.

- Python uses dynamic typing, in which a function’s variables, parameters, and return values can be any type. Also, the types of variables can change while the program runs.

- Generally, dynamic typing makes it easy to program and causes unexpected errors that you can only discover until the program runs.

- Python’s type hints provide you with optional static typing to leverage the best of both static and dynamic typing.

"""


# 1) The following example defines a simple function that accepts a string and returns another string:
def say_hi(name):
    return f"Hi {name}"


greeting = say_hi("John")
print(greeting)  # Hi John


# Here’s the syntax for adding type hints to a parameter and return value of a function:
# parameter: type
# -> type


# 2) For example, the following shows how to use type hints for the name parameter and return value of the say_hi() function:
def say_hiX(name: str) -> str:
    return f"Hi {name}"


# In this new syntax, the name parameter has the str type - name: str
# And the return value of the say_hi() function also has the type str - -> str


greetingX = say_hiX("John")
print(greetingX)  # Hi John


# Besides the str type, you can use other built-in types such as int, float, bool, and bytes for type hintings.
# It’s important to note that the Python interpreter ignores type hints completely. If you pass a number to the say_hi() function, the program will run without any warning or error:
greetingZ = say_hiX(123)
print(greetingZ)  # Hi 123

# To check the syntax for type hints, you need to use a static type checker tool.
