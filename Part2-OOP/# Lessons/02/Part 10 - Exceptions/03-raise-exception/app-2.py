"""
Reraise the current exception

- Sometimes, you want to log an exception and raise the same exception again. In this case, you can use the raise statement without specifying the exception object.

"""


# For example, the following defines a division() function that returns the division of two numbers:
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print("Logging exception:", str(ex))
        raise


# If you pass zero to the second argument of the division() function, the ZeroDivisionError exception will occur. However, instead of handling the exception, you can log the exception and raise it again.
# Note that you don’t need to specify the exception object in the raise statement. In this case, Python knows that the raise statement will raise the current exception that has been caught by the except clause.


# The following code causes a ZeroDivisionError exception:
division(1, 0)
# Logging exception: division by zero + trace
