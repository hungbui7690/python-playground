"""
Using subset operators

- Besides using the issubset() method, you can use the subset operator (<=) to check if a set is a subset of another set:

    set_a <= set_b


"""


# The subset operator (<=) returns True if set_a is a subset of the set_b. Otherwise, it returns False. For example:

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores <= numbers
print(result)  # True

result = numbers <= numbers
print(result)  # True


# The proper subset operator (<) check if the set_a is a proper subset of the set_b:

result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result)  # False
