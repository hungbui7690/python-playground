"""
Lists


"""


# 3) Removing elements from a list

# The del statement allows you to remove an element from a list by specifying the position of the element.
# The following example shows how to remove the first element from the list:

numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]

print(numbers)  # [3, 2, 7, 9, 4]


# The pop() method removes the last element from a list and returns that element:

numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()

print(last)  # 4
print(numbers)  # [1, 3, 2, 7, 9]


# Typically, you use the pop() method when you want to remove an element from a list and still want to access the value of that element.
# To pop an element by its position, you use the pop() with the element’s index. For example:

numbers = [1, 3, 2, 7, 9, 4]

second = numbers.pop(1)

print(second)  # 3
print(numbers)  # [1, 2, 7, 9, 4]


# To remove an element by value, you use the remove() method. Note that the remove() method removes only the first element it encounters in the list.
# For example, the following removes the element with value 9 from the numbers list:

numbers = [1, 3, 2, 7, 9, 4, 9]

numbers.remove(9)
print(numbers)  # [1, 3, 2, 7, 4, 9]

# In this example, the remove() method removes only the first number 9 but it doesn’t remove the second number 9 from the list.

"""
  Summary

      A list is an ordered collection of items.
      Use square bracket notation [] to access a list element by its index. The first element has an index 0.
      Use a negative index to access a list element from the end of a list. The last element has an index -1.
      Use list[index] = new_value to modify an element from a list.
      Use append() to add a new element to the end of a list.
      Use insert() to add a new element at a position in a list.
      Use pop() to remove an element from a list and return that element.
      Use remove() to remove an element from a list.

"""
