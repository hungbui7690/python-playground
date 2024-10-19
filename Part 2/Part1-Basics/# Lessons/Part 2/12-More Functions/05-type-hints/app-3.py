"""
Type hinting & type inference

    ~~ mypy app.py

"""

# When defining a variable, you can add a type hint like this:
name: str = "John"


# The type of name variable is str. If you assign a value that is not a string to the name variable, the static type checker will issue an error. For example:
# name = 100
# app.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")


# Adding a type to a variable is unnecessary because static type checkers typically can infer the type based on the value assigned to the variable.
# In this example, the value of the name is a literal string so that the static type checker will infer the type of the name variable as str. For example:
nameX = "Hello"
nameX = 100
# app.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")
