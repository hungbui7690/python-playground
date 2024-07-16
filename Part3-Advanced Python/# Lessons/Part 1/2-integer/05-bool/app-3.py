"""
How Python bool() constructor works under the hood

- The Boolean constructor bool() accepts an object and returns True or False.

- In Python, a class always contains a definition of how its instances evaluate to True and False. In other words, every object can be either True or False.

- All objects have a boolean value of True, except the following objects:

    None
    False
    0 in any numeric type such as integer, float, and decimal.
    Empty sequences e.g., list, tuple, string.
    Empty mapping types e.g., dictionary, set.
    Custom classes that implement __bool__() or __len__() methods that return False or 0.

…which have a boolean value of False

"""


# The __bool__() method
# When you pass an object to the bool() constructor, Python returns the value of the __bool__() method of that object.
def __bool__(self):
    return self != 0


"""
When you call:

    bool(200)

…Python actually executes:

    200.__bool__()

…and therefore returns the result of 200 != 0, which is True.


However, if you call:

    bool(0)

…Python executes:

    0.__bool__()

…and therefore returns the result of 0 != 0, which is False.

"""
