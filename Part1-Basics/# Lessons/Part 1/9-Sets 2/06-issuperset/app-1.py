"""
issuperset
- Suppose that you have two sets: A and B. A is a superset of B if all elements of B are elements of A.

- If A is a superset of B, then B is a subset of A. To check if a set is a subset of another, you use the issubset() method.

- If set A and set B are not equal, set A is a proper superset of set B.

- Logically, a set is a superset of itself.

"""


# The following example uses the issuperset() to check if the numbers set is a superset of the scores set:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers.issuperset(scores)
print(result)  # True
# Since all elements of the scores set are present in the numbers set, the numbers set is the superset of the scores set.


# A set is also a superset of itself. For example:

result = numbers.issuperset(numbers)
print(result)  # True


# The scores set is not a subset of the numbers set therefore the following example returns False:

result = scores.issuperset(numbers)
print(result)  # False
