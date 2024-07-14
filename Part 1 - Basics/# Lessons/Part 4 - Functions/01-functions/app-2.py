"""
Functions

"""


# Passing information to Python functions
# Suppose that you want to greet users by their names. To do it, you need to specify a name in parentheses of the function definition as follows:
# The name is called a function parameter or simply a parameter.
# When you add a parameter to the function definition, you can use it as a variable inside the function body:
def greet(name):
    print(f"Hi {name}")


# When you call a function with a parameter, you need to pass the information. For example:
greet("John")  # Hi John


# The value that you pass into a function is called an argument. In this example 'John' is an argument.
# Also, you can call the function by passing a variable into it:
first_name = "Jane"
greet(first_name)  # Hi Jane
# In this example, the first_name variable is also the argument of the greet() function.


"""
Parameters vs. Arguments

    Sometimes, parameters and arguments are used interchangeably. It’s important to distinguish between the parameters and arguments of a function.

    A parameter is a piece of information that a function needs. And you specify the parameter in the function definition. For example, the greet() function has a parameter called name.

    An argument is a piece of data that you pass into the function. For example, the text string 'John' or the variable jane is the function argument.
"""
