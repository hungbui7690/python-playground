"""
Adding slicing support

- To support slicing like this:

      fibonacci[1:5]

- …you need to add a logic to handle the slice object.

- In the fibonacci[1:5], the index argument of the __getitem__ method is a slice object whose start is 1 and stop is 5.

- And you can use the indices method of the slice object to get the indices of elements to return from the sequence:

      indices = index.indices(self.n)

- The self.n is the length of the sequence that will be sliced. In this case, it’s the number of elements in the Fibonacci sequence.

- To returns a list of Fibonacci from the slice, you can pass the indices to range function and use the list comprehension as follows:

      [Fibonacci.fib(k) for k in range(*indices)]

"""

from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
            return [Fibonacci.fib(k) for k in range(*indices)]

    @staticmethod
    @lru_cache
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n - 2) + Fibonacci.fib(n - 1)


fibonacci = Fibonacci(10)
print(fibonacci[1:5])  # [1, 2, 3, 5]


# Summary
# Implement the __len__ and __getitem__ method to define a custom sequence.
# The __getitem__ method need to returns an element based on a given index or raise an IndexError if the index is out of bounds.
