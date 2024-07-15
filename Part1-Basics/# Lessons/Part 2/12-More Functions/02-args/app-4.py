"""
Unpacking arguments


"""


# The following point function accepts two arguments and returns a string representation of a point with x-coordinate and y-coordinate:


def point(x, y):
    return f"({x},{y})"


# If you pass a tuple to the point function, you’ll get an error:
# TypeError: point() missing 1 required positional argument: 'y'
# a = (0, 0)
# origin = point(a)


# To fix this, you need to prefix the tuple a with the operator * like this:
a = (0, 0)
origin = point(*a)
print(origin)
