"""
enumerate

"""

fruits = ["Apple", "Orange", "Strawberry"]

e = enumerate(fruits, start=1)
print(type(e))  # <class 'enumerate'>


# The enumerate class has the __next__() method that returns a tuple:
print(e.__next__())  # (1, 'Apple')


# If you keep calling the __next__() method, it’ll return the next counting number with the value from the list:
print(e.__next__())  # (2, 'Orange')
print(e.__next__())  # (3, 'Strawberry')


# When all items in the list are iterated, calling the __next__() method will raise a StopIteration exception:
# print(e.__next__())  # StopIteration


# The enumerate() is functionally equivalent to the following function:
def enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1
