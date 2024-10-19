"""
Lookup Error

"""

# And you can catch either LookupError or Exception class when an IndexError exception occurs. For example:

colors = ["red", "green", "blue"]

try:
    print(colors[3])
except LookupError as e:
    print(e.__class__, "-", e)

print("Continue to run")
# <class 'IndexError'> - list index out of range
# Continue to run

# In this example, the exception is still IndexError even though we catch the LookupError exception. Therefore, when you handle an exception, the exception handler will catch the exception type you specify and any of its subclasses.
