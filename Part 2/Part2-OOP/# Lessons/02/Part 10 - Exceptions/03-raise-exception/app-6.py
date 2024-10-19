"""
Python raise from


"""


# The following modifies the above code to show the __cause__ attribute of the ValueError exception:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not be zero") from ex


try:
    divide(10, 0)
except ValueError as ex:
    print("cause:", ex.__cause__)
    print("exception:", ex)
# cause: division by zero
# exception: b must not be zero
