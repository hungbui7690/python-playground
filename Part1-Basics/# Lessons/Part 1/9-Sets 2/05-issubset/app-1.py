"""
issubset
- to check if a set is a subset of another set.
- Suppose that you have two sets A and B. Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.
- Set A and set B can be equal. If set A and set B are not equal, A is a proper subset of B.

- In Python, you can use the Set issubset() method to check if a set is a subset of another:

    set_a.issubset(set_b)

- If the set_a is a subset of the set_b, the issubset() method returns True. Otherwise, it returns False.

"""


# The following example uses the issubset() method to check if the set_a is a subset of the set_b:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers))  # True


# By definition, a set is also a subset of itself. The following example returns True:

print(numbers.issubset(numbers))  # True


# The following example returns False because some elements in the numbers set aren’t in the scores set. In other words, the numbers set is not a subset of the scores set:

print(numbers.issubset(scores))  # False
