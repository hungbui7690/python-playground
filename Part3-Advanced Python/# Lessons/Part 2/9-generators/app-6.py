"""
GENERATOR EXPRESSION


"""

# The following example defines a generator expression that returns square numbers of integers from 0 to 4:
squares = (n**2 for n in range(5))


# Since the squares is a generator object, you can iterate over its elements like this:
for square in squares:
    print(square)
# 0
# 1
# 4
# 9
# 16


"""
As you can see, instead of using a function to define a generator function, you can use a generator expression.

A generator expression is like a list comprehension in terms of syntax. For example, a generator expression also supports complex syntaxes including:

    if statements
    Multiple nested loops
    Nested comprehensions

However, a generator expression uses the parentheses () instead of square brackets [].
"""
