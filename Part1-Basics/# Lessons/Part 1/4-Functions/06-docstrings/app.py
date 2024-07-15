"""
Docstrings
- Python provides a built-in function called help() that allows you to show the documentation of a function.

"""

# The following example shows the documentation of the print() function:
help(print)
# Note that you can use the help() function to show the documentation of modules, classes, functions, and keywords. This tutorial focuses on function documentation only.


# Using docstrings to document functions
# To document your functions, you can use docstrings. The PEP 257 provides the docstring conventions.
# When the first line in the function body is a string, Python will interpret it as a docstring. For example:
def add(a, b):
    "Return the sum of two arguments"
    return a + b


# And you can use the help() function to find the documentation of the add() function:
help(add)


# Typically, you use multi-line docstrings:
def addX(a, b):
    """Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b


help(addX)


"""
    - Python stores the docstrings in the __doc__ property of the function.
    - The following example shows how to access the __doc__ property of the add() function:
    add.__doc__


    Summary
    - Use the help() function to get the documentation of a function.
    - Place a string, either single-line or multi-line strings, as the first line in the function to add documentation to it.
"""
