"""
Disjoint Sets
- Two sets are disjoint when they have no elements in common. In other words, two disjoint sets are sets whose intersection is an empty set.

- In Python, you use the Set isdisjoint() method to check if two sets are disjoint or not:

    set_a.isdisjoint(set_b)

- The isdisjoint() method returns True if the set_a and set_b are disjoint. Otherwise, it returns False.
- The isdisjoint() method also accepts any iterable, not just a set.
- If you pass a list, a tuple, or a dictionary, the isdisjoint() method will convert it to a set before checking.

"""


# The following example uses the isdisjoint() method to check if the set odd_numbers and set even_numbers are disjoint:

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)  # True
# Since no elements in the odd_numbers are present in the set even_numbers, the isdisjoint() method returns True.


# The following example uses the isdisjoint() method to check if the set letters and the set alphanumerics are disjoint:

letters = {"A", "B", "C"}
alphanumerics = {"A", 1, 2}

result = letters.isdisjoint(alphanumerics)
print(result)  # False
# It returns False because the letter 'A' in the set alphanumerics is present in the set letters.


# The following example passes a list to the isdisjoint() method instead of a set:
letters = {"A", "B", "C"}
result = letters.isdisjoint([1, 2, 3])
print(result)  # True
