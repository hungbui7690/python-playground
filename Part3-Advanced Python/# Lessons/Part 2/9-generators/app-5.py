"""
GENERATOR EXPRESSION

Introduction to generator expressions

- A generator expression is an expression that returns a generator object.

- Basically, a generator function is a function that contains a yield statement and returns a generator object.

"""


# For example, the following defines a generator function:
def squares(length):
    for n in range(length):
        yield n**2


# The squares generator function returns a generator object that produces square numbers of integers from 0 to length - 1.
# Because a generator object is an iterator, you can use a for loop to iterate over its elements:
for square in squares(5):
    print(square)
# 0
# 1
# 4
# 9
# 16


# A generator expression provides you with a more simple way to return a generator object.
