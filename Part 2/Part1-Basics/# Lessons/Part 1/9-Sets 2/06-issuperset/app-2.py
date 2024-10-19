"""
Using superset operators

- The >= operator determines if a set is a superset of another set:

    set_a >= set_b

- To check if a set is a proper superset of another set, you use the > operator:

    set_a > set_b

"""


# The >= operator returns True if the set_a is a superset of the set_b. Otherwise, it returns False. For example:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers >= scores
print(result)  # True

result = numbers >= numbers
print(result)  # True


# To check if a set is a proper superset of another set, you use the > operator:

result = numbers > scores
print(result)  # True

result = numbers > numbers
print(result)  # False

# In this example, the set numbers is not a proper superset of itself, therefore, the > operator returns False.
