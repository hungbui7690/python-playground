"""
FIBONACCI SEQUENCE

Introduction to the custom Sequence type in Python

- Sometimes, it’s useful to implement a custom sequence type that has functions similar to the built-in sequence type like tuples and lists.

- As you’ve learned so far, a sequence can be mutable or immutable. In this tutorial, you’ll focus on defining a custom immutable sequence type.

- Basically, an immutable sequence type should support two main functions:

    Return the number of elements of the sequence. Technically, this requirement is not necessary.
    Return an element at a given index or raise an IndexError if the index is out of bounds.

- If an object can fullfil the above requirements, then you can:

    Use the square brackets [] syntax to retrieve an element by an index.
    Iterate over the elements of the sequence using the for loop, comprehension, etc.

- Technically, a custom sequence type needs to implement the following methods:

    __getitem__ – returns an element at a given index.

      + The __getitem__ method has the index argument which is an integer. The ___getitem__ should return an element from the sequence based on the specified index.

      + The range of the index should be from zero to length - 1. If the index is out of bounds, the __getitem__ method should raise an IndexError exception.

      + Also, the __getitem__ method can accept a slice object to support slicing.

    __len__ – returns the length of the sequence.

      + If a custom sequence has the __len__ method, you can use the built-in len function to get the number of elements from the sequence.

\\\\\\\\\\\\\\\\\\\

Introduction to the Fibonacci sequence

- The Fibonacci sequence was first discovered by Leonardo Fibonacci, who is an Italian mathematician, around A.D. 1170.

- In the Fibonacci sequence, each number is the sum of two numbers that precede it. For example:

      1, 1, 2, 3, 5, 8 , 13, 21, ...

- The following formula describes the Fibonacci sequence:

      f(1) = 1
      f(2) = 1
      f(n) = f(n-1) + f(n-2) if n > 2

- Some sources state that the Fibonacci sequence starts at zero, not 1 like this:

      0, 1, 1, 2, 3, 5, 8 , 13, 21, ...

- But we’ll stick with the original Fibonacci sequence that starts at one.

"""


# To calculate a Fibonacci number in Python, you define a recursive function as follows:
# In this recursive function, the fib(1) and fib(2) always returns 1. And when n is greater than 2, the fib(n) = fib(n-2) – fib(n-1)
def fib(n):
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


# The following adds a statement at the beginning of the fib function for the logging debugging purpose:
def fibX(n):
    print(f"Calculate Fibonacci of {n}")
    if n < 2:
        return 1
    return fibX(n - 2) + fibX(n - 1)


fibX(6)

# If we run this, it has a lot of output
# As shown clearly from the output, the fib function has many repetitions.
# For example, it has to calculate the Fibonacci of 3 three times. This is not efficient.
# To solve this, Python provides a decorator called lru_cache from the functools module.
