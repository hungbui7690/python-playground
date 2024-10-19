"""
Python raise exception from None
- If the cause of the exception is not important, you can omit the cause by using the raise exception from None statement:

        raise <ExceptionType> from None

"""


#  For example, you can hide the cause of the ValueError exception in the divide() function as follows:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("b must not be zero") from None


try:
    divide(10, 0)
except ValueError as ex:
    print("cause:", ex.__cause__)
    print("exception:", ex)
# cause: None
# exception: b must not be zero


# Now, the __cause__ is None. Also, the divide() function raises the ValueError exception without any additional information.s
