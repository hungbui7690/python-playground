"""
Python Custom Exception
- To create a custom exception class, you define a class that inherits from the built-in Exception class or one of its subclasses such as ValueError class: pic

"""


#  The following example defines a CustomException class that inherits from the Exception class:
class CustomException(Exception):
    """my custom exception class"""


# Note that the CustomException class has a docstring that behaves like a statement. Therefore, you don’t need to add the pass statement to make the syntax valid.


# To raise the CustomException, you use the raise statement. For example, the following uses the raise statement to raise the CustomException:
try:
    raise CustomException("This is my custom exception")
except CustomException as ex:
    print(ex)
# This is my custom exception


"""
Like standard exception classes, custom exceptions are also classes. Hence, you can add functionality to the custom exception classes like:

    Adding attributes and properties.
    Adding methods e.g., log the exception, format the output, etc.
    Overriding the __str__ and __repr__ methods
    And doing anything else that you can do with regular classes.

In practice, you’ll want to keep the custom exceptions organized by creating a custom exception hierarchy. The custom exception hierarchy allows you to catch exceptions at multiple levels, like the standard exception classes.
"""
