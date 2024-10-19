"""
Unpacking Tuple


"""

# Python defines a tuple using commas (,), not parentheses (). For example, the following defines a tuple with two elements:
x = 1, 2
print(x)


# Python uses the parentheses to make the tuple clearer:
x = (1, 2)
print(x)


# Python also uses the parentheses to create an empty tuple:
x = ()
print(x)


# In addition, you can use the tuple() constructor like this:
x = tuple()
print(x)


# To define a tuple with only one element, you still need to use a comma. The following example illustrates how to define a tuple with one element:
x = (1,)
print(x)


# It’s equivalent to the following:
x = (1,)
print(x)


# Note that the following is an integer, not a tuple:
x = 1
print(x)
