"""
Iterables
- In Python, an iterable is an object that includes zero, one, or many elements. An iterable has the ability to return its elements one at a time.

- Because of this feature, you can use a for loop to iterate over an iterable.



"""


# In fact, the range() function is an iterable because you can iterate over its result:

for index in range(3):
    print(index)


# Also, a string is an iterable because you can use a for loop to iterate over it:

str = "Iterables"
for ch in str:
    print(ch)


# Lists and tuples are also iterables because you can loop over them. For example:

ranks = ["high", "medium", "low"]

for rank in ranks:
    print(rank)

# The rule of thumb is that if you know if can loop over something, it’s iterable.
