"""
Lists


"""


# 2) Adding elements to the list

# The append() method appends an element to the end of a list. For example:
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)

print(numbers)  # [1, 3, 2, 7, 9, 4, 100]


# The insert() method adds a new element at any position in the list.
# For example, the following inserts the number 100 at index 2 of the numbers list:

numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)

print(numbers)  # [1, 3, 100, 2, 7, 9, 4]
