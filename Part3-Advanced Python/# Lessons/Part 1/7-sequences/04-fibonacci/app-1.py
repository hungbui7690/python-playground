"""
FIBONACCI SEQUENCE


"""

from functools import lru_cache


# First, define a class that implements the Fibonacci sequence:
class Fibonacci:
    # The __init__ method accepts an integer n that specifies the length of the sequence.
    def __init__(self, n):
        self.n = n

    # Second, define a static method that calculates a Fibonacci number of an integer:
    @staticmethod
    @lru_cache(2**16)
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n - 2) + Fibonacci.fib(n - 1)

    # Third, implement the __len__ method so that you can use the built-in len function to get the number of elements from the Fibonacci sequence:
    def __len__(self):
        return self.n

    # Finally, implement the __getitem__ method to support indexing through the square brackets syntax:
    # The __getitem__ method accepts an index which is an integer. The __getitem__ checks if the index is integer by using the isinstance function.
    # The __getitem__ method raises the IndexError exception if the index is out of bounds. Otherwise, it returns the Fibonacci number of the index.
    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)


fibonacci = Fibonacci(10)


# access elements via indices
print("Accessing Fibonacci sequence using []:")
print(fibonacci[0])  # 1
print(fibonacci[1])  # 1
print(fibonacci[2])  # 2


print("Accessing Fibonacci sequence using for loop:")
# using for loop
for f in fibonacci:
    print(f)

"""
Accessing Fibonacci sequence using for loop:
1
1
2
3
5
8
13
21
34
55
"""
