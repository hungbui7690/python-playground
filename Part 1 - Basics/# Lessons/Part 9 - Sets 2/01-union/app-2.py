"""
The union() method vs. set union operator

- In fact, the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.

"""

# The following example shows how to pass a list to the union() method:

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)  # {1, 2, 3, 4}


# However, the union operator (|) only allows sets, not iterables like the union() method.
# The following example causes an error:
# TypeError: unsupported operand type(s) for |: 'set' and 'list'
# ratings = rates | ranks


# In conclusion, the union() method accepts the iterables while the union operator only allows sets.
