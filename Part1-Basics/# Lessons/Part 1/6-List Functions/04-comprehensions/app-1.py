"""
List Comprehensions
- allow you to create a new list from an existing one.

- Syntax
    squares = [number**2 for number in numbers]

"""

# For example, suppose that you have a list of five numbers like this:

numbers = [1, 2, 3, 4, 5]


# And you want to get a list of squares based on this numbers list
# The straightforward way is to use a for loop:

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)  # [1, 4, 9, 16, 25]

"""
  In this example, the for loop iterates over the elements of the numbers list, squares each number and adds the result to the squares list.

  Note that a square number is the product of the number multiplied by itself. For example, square number 2 is 2*2 = 4, square number of 3 is 3*3 = 9, and so on.
"""


# To make the code more concise, you can use the built-in map() function with a lambda expression:

squares = list(map(lambda number: number**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]


"""
  Since the map() function returns an iterator, you need to use the list() function to convert the iterator to a list.

  Both the for loop and map() function can help you create a new list based on an existing one. But the code isn’t really concise and beautiful.

  To help you create a list based on the transformation of elements of an existing list, Python provides a feature called list comprehensions.
"""


# The following shows how to use list comprehension to make a list of squares from the numbers list:

squares = [number**2 for number in numbers]
print(squares)


"""
  And here’s the list comprehension part:

      squares = [number**2 for number in numbers]

  A list comprehension consists of the following parts:

      An input list (numbers)
      A variable that represents the elements of the list (number)
      An output expression (number**2) that returns the elements of the output list from the elements of the input list.

  The following shows the basic syntax of the Python list comprehension:

      [output_expression for element in list]

  It’s equivalent to the following:

      output_list = []
      for element in list:
          output_list.append(output_expression)

"""
