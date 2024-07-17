"""
FIBONACCI SEQUENCE


"""

from functools import lru_cache


# The lru_cache allows you to cache the result of a function. When you pass the same argument to the function, the function just gets the result from the cache instead of recalculating it.
# The following shows how to use the lru_cache decorator to speed up the fib function:
@lru_cache
def fib(n):
    print(f"Calculate the Fibonacci of {n}")
    if n < 2:
        return 1
    return fib(n - 2) + fib(n - 1)


fib(6)
# Calculate the Fibonacci of 6
# Calculate the Fibonacci of 4
# Calculate the Fibonacci of 2
# Calculate the Fibonacci of 0
# Calculate the Fibonacci of 1
# Calculate the Fibonacci of 3
# Calculate the Fibonacci of 5

# As shown clearly from the output, the number of calculations is reduced significantly.
