"""
Extended unpacking using the * operator


"""

# Sometimes, you don’t want to unpack every single item in a tuple. For example, you may want to unpack the first and second elements. In this case, you can use the * operator. For example:

r, g, *other = (192, 210, 100, 0.5)
print(other)  # [100, 0.5]


# Notice that you can only use the * operator once on the left-hand side of an unpacking assignment.
# The following example results in error:

# x, y, *z, *t = (10, 20, 30, "10:30")
# SyntaxError: multiple starred expressions in assignment
