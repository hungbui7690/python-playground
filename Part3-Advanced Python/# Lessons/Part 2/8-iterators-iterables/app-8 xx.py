"""
PYTHON ITER

Introduction to the Python iter function

"""


# The following adds the __getitem__() method to the Counter class:
class Counter:
    def __init__(self):
        self.__current = 0

    def __getitem__(self, index):
        if isinstance(index, int):
            self.current += 1
            return self.current


# Because the Counter implements the __getitem__() method that returns an element based on an index, it’s a sequence.
# Now, you can use the iter() function to get the iterator of the counter:
counter = Counter()

iterator = iter(counter)
print(type(iterator))  # <class 'iterator'>


# In this case, Python creates an iterator object and returns it. Hence, you can use the iterator object to iterate the counter:
for _ in range(1, 4):
    print(next(iterator))
