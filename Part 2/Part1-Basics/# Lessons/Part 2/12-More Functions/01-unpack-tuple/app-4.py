"""
ValueError: too many values to unpack


"""

# The following example unpacks the elements of a tuple into variables. However, it’ll result in an error:
# ValueError: too many values to unpack (expected 2)

# x, y = 10, 20, 30
# This error is because the right-hand side returns three values while the left-hand side only has two variables.


# To fix this, you can add a _ variable:

x, y, _ = 10, 20, 30
# The _ variable is a regular variable in Python. By convention, it’s called a dummy variable.
# Typically, you use the dummy variable to unpack when you don’t care and use its value afterward.
