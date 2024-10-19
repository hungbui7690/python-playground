"""
Using Python context manager to implement the start and stop pattern

"""


# The following defines a Timer class that supports the context manager protocol:

from time import perf_counter


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


"""
How it works.
    First, import the perf_counter from the time module.
    Second, start the timer in the __enter__ method
    Third, stop the timer in the __exit__ method and return the elapsed time.
"""


# Now, you can use the Timer class to measure the time needed to calculate the Fibonacci of 1000, one million times:


def fibonacci(n):
    f1 = 1
    f2 = 1
    for i in range(n - 1):
        f1, f2 = f2, f1 + f2

    return f1


with Timer() as timer:
    for _ in range(1, 10000):
        fibonacci(10)

print(timer.elapsed)


# Summary
# Use Python context managers to define runtime contexts when executing in the with statement.
# implement the __enter__() and __exit__() methods to support the context manager protocol.
