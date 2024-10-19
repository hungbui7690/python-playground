"""
Set intersection() method vs set intersection operator (&)
- Set intersection operator & only allows sets,
- Set intersection() method can accept any iterables, like strings, lists, and dictionaries.

- If you pass iterables to the intersection() method, it’ll convert the iterables to set before intersecting them.

- However, the set intersection operator (&) will raise an error if you use it with iterables.

"""

# The following example uses the intersection() method to intersect a set with a list:

numbers = {1, 2, 3}
scores = [2, 3, 4]

numbers = numbers.intersection(scores)
print(numbers)  # {2, 3}


# If you use the set intersection operator (&) instead, you’ll get an error:
# TypeError: unsupported operand type(s) for &: 'set' and 'list'
# numbers = numbers & scores
