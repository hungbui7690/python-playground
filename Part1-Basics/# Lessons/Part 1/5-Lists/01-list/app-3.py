"""
Lists
- A list is dynamic. It means that you can modify elements in the list, add new elements to the list, and remove elements from a list.

"""


# 1) Modifying elements in a list
# To change an element, you assign a new value to it using this syntax:
#   list[index] = new_value

# The following example shows how to change the first element of the numbers list to 10:
numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10

print(numbers)  # [10, 3, 2, 7, 9, 4]


# The following shows how to multiply the second element by 10:
numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1] * 10

print(numbers)  # [1, 30, 2, 7, 9, 4]


# And the following divides the third element by 2:

numbers = [1, 3, 2, 7, 9, 4]
numbers[2] /= 2

print(numbers)  # [1, 3, 1.0, 7, 9, 4]
