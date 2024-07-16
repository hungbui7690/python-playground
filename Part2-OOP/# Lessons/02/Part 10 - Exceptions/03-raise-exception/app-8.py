"""
Python raise exception from None
- If the cause of the exception is not important, you can omit the cause by using the raise exception from None statement:

        raise <ExceptionType> from None

"""


#  If you remove the try statement in the code that calls the divide() function:


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("b must not be zero") from None


divide(10, 0)
# ValueError: b must not be zero


# Summary
# Use the Python raise from statement to modify and forward an existing exception.
# Use the raise exception from None statement to hide the cause of the exception.
