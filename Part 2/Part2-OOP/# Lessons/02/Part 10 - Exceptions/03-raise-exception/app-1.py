"""
Python Raise Exception
- To raise an exception, you use the raise statement:

    raise ExceptionType()

- The ExceptionType() must be subclass of the BaseException class. Typically, it is a subclass of the Exception class. Note that the ExceptionType doesn’t need to be directly inherited from the Exception class. It can indirectly inherit from a class that is a subclass of the Exception class.

- The BaseException class has the __init__ method that accepts an *args argument. It means that you can pass any number of arguments to the exception object when raising an exception.

"""

# The following example uses the raise statement to raise a ValueError exception. It passes three arguments to the ValueError __init__ method:

try:
    raise ValueError("The value error exception", "x", "y")
except ValueError as ex:
    print(ex.args)

# ('The value error exception', 'x', 'y')
