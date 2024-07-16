"""
Python raise from
- The raise from statement has the following syntax:

    raise <ExceptionType> from <cause>

- Technically, it’s equivalent to the following:

    ex = ExceptionType
    ex.__cause__ = cause
    raise ex

- By default, the __cause__ attribute on exception objects is always initialized to None.

"""


# The following divide() function divides a number by another and returns the result of the division:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not be zero")


divide(10, 0)
"""
Traceback (most recent call last):
  File "c:/python/app.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero

@@ During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:/python/app.py", line 8, in <module>
    divide(10, 0)
  File "c:/python/app.py", line 5, in divide
    raise ValueError('b must not be zero')
ValueError: b must not be zero
"""
