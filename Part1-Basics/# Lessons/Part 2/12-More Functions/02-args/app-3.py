"""
Python *args argument exhausts positional arguments

- If you use the *args argument, you cannot add more positional arguments. However, you can use keyword arguments.


"""


def add(x, y, *args, z):
    return x + y + sum(args) + z


# The following example results in an error because it uses a positional argument after the *arg argument:
# TypeError: add() missing 1 required keyword-only argument: 'z'

add(10, 20, 30, 40, 50)


# To fix it, you need to use a keyword argument after the *args argument as follows:

add(10, 20, 30, 40, z=50)
# In this example, Python assigns 10 to x, 20 to y,(30,40) to args, and 50 to z.
