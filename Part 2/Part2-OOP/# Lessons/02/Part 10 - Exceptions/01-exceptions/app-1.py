"""
Python Exceptions
- In Python, exceptions are objects of the exception classes. All exception classes are the subclasses of the BaseException class.

- However, almost all built-in exception classes inherit from the Exception class, which is the subclass of the BaseException class: pic-1

- This page shows a complete class hierarchy for built-in exceptions in Python.
- https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

# The following example defines a list of three elements and attempts to access the fourth one:

colors = ["red", "green", "blue"]
print(colors[3])  # IndexError: list index out of range

# When an exception occurs, Python stops the program unless you handle it.
