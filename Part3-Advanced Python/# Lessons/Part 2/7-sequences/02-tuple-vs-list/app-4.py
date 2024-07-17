"""
Tuple vs List


"""

from timeit import timeit


# The following compares the time that needs to copy a list and a tuple 1 million times:
times = 1_000_000

t1 = timeit("list(['apple', 'orange', 'banana'])", number=times)
print(f"Time to copy a list {times} times: {t1}")

t2 = timeit("tuple(('apple', 'orange', 'banana'))", number=times)
print(f"Time to copy a tuple {times} times: {t2}")

diff = "{:.0%}".format((t2 - t1) / t1)

print(f"difference: {diff}")


# Summary
# A tuple is immutable while a list is mutable.
# The storage efficiency of a tuple is greater than a list.
# Copying a tuple is slightly faster than a list.
# Use a tuple if you don’t intend to mutable it.
