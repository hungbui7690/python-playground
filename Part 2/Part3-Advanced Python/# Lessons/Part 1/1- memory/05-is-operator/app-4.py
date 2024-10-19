"""
Python is not operator

- To negate the is operator, you use the not operator. The is not operator returns False if two variables reference the same object. Otherwise, it returns True.

"""

# The following example uses the is not operator to check if the two variables don’t reference the same list object:

ranks = [1, 2, 3]
rates = [1, 2, 3]

result = ranks is not rates
print(result)  # True


# Summary
# Use the is operator to check if two variables reference the same object.
# Use the is operator to check two variables for identity and == to check for two variables for equality.
# Use the not operator to negate the result of the is operator.
