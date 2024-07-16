"""
Python is operator vs == operator

- The equality operator (==) compares two variables for equality and returns True if they are equal. Otherwise, it returns False.

"""

# The following example uses both is operator and == operator:
a = 100
b = a

is_identical = a is b
is_equal = a == b

print(is_identical)  # True
print(is_equal)  # True

# Since a and b references the same object, they’re both identical and equal.


# In the following example, both lists have the same elements, so they’re equal.
# However, since they reference different list objects in the memory, they’re not identical:
ranks = [1, 2, 3]
rates = [1, 2, 3]

is_identical = ranks is rates
is_equal = ranks == rates

print(is_identical)  # False
print(is_equal)  # True
