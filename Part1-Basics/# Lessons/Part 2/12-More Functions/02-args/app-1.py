"""
Python *args


"""

# Tuple unpacking

# The following unpacks a tuple into two variables:

x, y = 10, 20

# Python assigns 10 to x and 20 to y. It’s similar to passing two arguments to a function:


def add(x, y):
    return x + y


add(10, 20)

# In this example, Python passed 10 to x and 20 to y.


# Similarly, the following assigns 10 to x, 20 to y, and the list [30, 40] to z:

x, y, *z = 10, 20, 30, 40

print(x)
print(y)
print(z)  # [30, 40]


# Python uses the same concept for the function arguments. For example:


def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)
print(result)  # 100


# The add function accepts three parameters x, y, and *args. The *args is a special argument preceded by a star (*).
# When passing the positional arguments 10, 20, 30, and 40 to the function, Python assigns 10 to x, 20 to y, and a tuple (30, 40) to args.
# It’s like tuple unpacking except that the args is a tuple, not a list.
