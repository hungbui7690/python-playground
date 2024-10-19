"""
Lists

"""

# Accessing elements in a list
# Since a list is an ordered collection, you can access its elements by indexes like this:
# list[index]

# Lists are zero-based indexes. In other words, the first element has an index of 0, the second element has an index of 1, and so on.
# For example, the following shows how to access the first element of the numbers list:

numbers = [1, 3, 2, 7, 9, 4]

print(numbers[0])  # 1


# The numbers[1] will return the second element from the list:

print(numbers[1])  # 3


# The negative index allows you to access elements starting from the end of the list.
# The list[-1] returns the last element. The list[-2] returns the second last element, and so on. For example:

print(numbers[-1])  # 4
print(numbers[-2])  # 9
