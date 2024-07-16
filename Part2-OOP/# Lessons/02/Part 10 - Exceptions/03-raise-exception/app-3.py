"""
Raise another exception during handling an exception

"""


# When handling an exception, you may want to raise another exception. For example:
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not zero")


# In the division() function, we raise a ValueErrorException if the ZeroDivisionError occurs.
# If you run the following code, you’ll get the detail of the stack trace:
division(1, 0)
# First, the ZeroDivisionError exception occurs
# Second, during handling the ZeroDivisionError exception, the ValueError exception occurs


# Summary
# Use the Python raise statement to raise an exception.
# When handling exception, you can raise the same or another exception.
