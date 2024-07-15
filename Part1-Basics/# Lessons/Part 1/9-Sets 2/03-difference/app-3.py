"""
The set difference() method vs set difference operator (-)
- The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) while the set difference operator (-) only allows sets.

- When you pass iterables to the set difference() method, it’ll convert the iterables to sets before performing the difference operation.

"""


# The following shows how to use the set difference() method with a list:

scores = {7, 8, 9}
numbers = [9, 10]

new_scores = scores.difference(numbers)
print(new_scores)


# However, if you use the set difference operator (-) with iterables, you’ll get an error:
# TypeError: unsupported operand type(s) for -: 'set' and 'list'

new_scores = scores - numbers
print(new_scores)
