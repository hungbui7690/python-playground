"""
List Comprehensions
- allow you to create a new list from an existing one.


"""

# Python list comprehension with if condition
# The following shows a list of the top five highest mountains on Earth:

mountains = [
    ["Makalu", 8485],
    ["Lhotse", 8516],
    ["Kanchendzonga", 8586],
    ["K2", 8611],
    ["Everest", 8848],
]

# To get a list of mountains where the height is greater than 8600 meters, you can use a for loop or the filter() function with a lambda expression like this:

highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))
print(highest_mountains)  # [['K2', 8611], ['Everest', 8848]]


"""
  Like the map() function, the filter() function returns an iterator. Therefore, you need to use the list() function to convert the iterator to a list.

  Python List comprehensions provide an optional predicate that allows you to specify a condition for the list elements to be included in the new list:

      [output_expression for element in list if condition]
"""

# This list comprehension allows you to replace the filter() with a lambda expression:

highest_mountains = [m for m in mountains if m[1] > 8600]
print(highest_mountains)  # [['K2', 8611], ['Everest', 8848]]


"""
  Summary

      Python list comprehensions allow you to create a new list from an existing one.
      Use list comprehensions instead of map() or filter() to make your code more concise and readable.
"""
