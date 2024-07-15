"""
STRING JOIN

"""

# 2) Using string join() method to concatenate non-string data into a string
# The following example uses the join() method to concatenate strings and numbers in a tuple to a single string:
# TypeError: sequence item 1: expected str instance, int found
# It issued a TypeError because the tuple product has two integers.
product = ("Laptop", 10, 699)
# result = ",".join(product)


# To concatenate elements in the tuple, you’ll need to convert them into strings before concatenating. For example:
product = ("Laptop", 10, 699)
result = ",".join(str(p) for p in product)
print(result)  # Laptop,10,699


# How it works.
# First, use a generator expression to convert each element of the product tuple to a string.
# Second, use the join() method to concatenate the string elements
