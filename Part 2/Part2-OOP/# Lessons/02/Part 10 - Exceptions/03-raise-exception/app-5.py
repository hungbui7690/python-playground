"""
Python raise from


"""


# To instruct Python that you want to modify and forward the ZeroDivisionError exception, you can use the raise from statement like this:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not be zero") from ex


divide(10, 0)
"""
Traceback (most recent call last):
  File "c:/python/app.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero

@@ The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "c:/python/app.py", line 8, in <module>
    divide(10, 0)
  File "c:/python/app.py", line 5, in divide
    raise ValueError('b must not be zero') from ex
ValueError: b must not be zero
"""

# Now, you receive the ValueError exception with a cause added to the __cause__ attribute of the exception object.
