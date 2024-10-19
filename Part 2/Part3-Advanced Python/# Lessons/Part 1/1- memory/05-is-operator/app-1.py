"""
is Operator
- Python is operator compares two variables and returns True if they reference the same object. If the two variables reference different objects, the is operator returns False.

- In other words, the is operator compares the identity of two variables and returns True if they reference the same object.

"""

# Let’s take a look at the following example:
a = 100
b = a  # define variable b that references the same object referenced by the a variable.
result = a is b
print(result)  # True
# Since both a and b reference the same object, the result is True.


# The following example defines two variables a and b and initialize them to 100:
a = 100
b = 100
result = a is b
print(result)  # True
# In this example, there’s no link between a and b. However, when you assign 100 to b, Python Memory Manager reuses the existing object. Therefore, both a and b references the same object:
