"""
The symmetric_difference() method vs symmetric difference operator (^)
- The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.

- If the iterables aren’t sets, the method will convert them to sets before returning the symmetric difference of them.

"""


# The following example shows how to use the symmetric_difference() method to find the symmetric difference between a set and a list:

scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)

print(new_set)  # {10, 7}


# However, the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error. For example:
# TypeError: unsupported operand type(s) for ^: 'set' and 'list'
new_set = scores ^ ratings
