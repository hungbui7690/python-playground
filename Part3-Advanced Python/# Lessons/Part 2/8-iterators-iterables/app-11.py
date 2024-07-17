"""
The second form of the Python iter() function


"""


def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


# Third, define a new counter iterator:
class CounterIterator:
    def __init__(self, fn, sentinel):
        self.fn = fn
        self.sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        current = self.fn()
        if current == self.sentinel:
            raise StopIteration

        return current


"""
The CounterIterator‘s constructor accepts a callable fn and a sentinel.

The __next__() method returns the value returned by the callable (fn) or raise a StopIteration exception if the return value equals the sentinel.
"""


# Instead of defining a new iterator every time you want to iterate values returned by the callable, you can use the iter(callable, sentinel) function:
cnt = counter()
iterator = CounterIterator(cnt, 4)
for count in iterator:
    print(count)
# 1
# 2
# 3
