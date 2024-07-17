"""
Use Python iter() function to test if an object is iterable

- To determine whether an object is iterable, you can check if it implements the __iter__() or __getitem__() method.

"""


# However, you can use the iter() function to test if an object is iterable as follows:
def is_iterable(object):
    try:
        iter(object)
    except TypeError:
        return False
    else:
        return True


# If the object doesn’t implement neither __iter__() method nor __getitem__() method, the iter() function raises the TypeError exception.
# The following shows how to use the is_iterable() function:
print(is_iterable([1, 2, 3]))  # True
print(is_iterable("Python iter"))  # True
print(is_iterable(100))  # False
