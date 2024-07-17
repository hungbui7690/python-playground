"""
PYTHON ITER

Introduction to the Python iter function

- The iter function returns an iterator of a given object:

        iter(object)

- The iter function requires an argument that can be an iterable or a sequence. In general, the object argument can be any object that supports either iteration or sequence protocol.

- When you call the iter function on an object, the function first looks for an __iter__() method of that object.

- If the __iter__ method exists, the iter function calls it to get an iterator. Otherwise, the iter function will look for a __getitem__ method.

- If the __getitem__ is available, the iter function creates an iterator object and returns that object. Otherwise, it raises a TypeError exception.

- The following flowchart illustrates how the iter function works: pic-1


"""


# The following example defines a simple Counter class and uses the iter() function to get an iterator of the counter object:
class Counter:
    def __init__(self):
        self.__current = 0


counter = Counter()

# It’ll raise a TypeError because the counter object is not an iterable (missing __iter__ or __getItem__ )
iterator = iter(counter)  # TypeError: 'Counter' object is not iterable
