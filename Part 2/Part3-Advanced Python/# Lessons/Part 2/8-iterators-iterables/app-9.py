"""
PYTHON ITER

Introduction to the Python iter function

"""


# The following adds the CounterIterator class to the Counter class and implement the iterable protocol:
class Counter:
    def __init__(self):
        self.current = 0

    def __getitem__(self, index):
        if isinstance(index, int):
            self.current += 1
            return self.current

    def __iter__(self):
        return self.CounterIterator(self)

    class CounterIterator:
        def __init__(self, counter):
            self.__counter = counter

        def __iter__(self):
            return self

        def __next__(self):
            self.__counter.current += 1
            return self.__counter.current


"""
How it works.

    The Counter class implements the __iter__() method that returns an iterator. The return iterator is a new instance of the CounterIterator.
    The CounterIterator class supports the iterator protocol by implementing the __iter__() and __next__() methods.

When both __iter__() and __getitem__() methods exist, the iter() function always uses the __iter__() method:
"""


counter = Counter()

iterator = iter(counter)
print(type(iterator))  # <class '__main__.Counter.CounterIterator'>


for _ in range(1, 4):
    print(next(iterator))
# 1
# 2
# 3


# In this example, the iter() function calls the __iter__() method instead of __getitem__() method. That’s why you see the CounterIterator in the output.
