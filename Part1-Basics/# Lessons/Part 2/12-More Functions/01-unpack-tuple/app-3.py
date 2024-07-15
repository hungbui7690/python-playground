"""
Using unpacking tuple to swap values of two variables


"""

# Traditionally, to swap the values of two variables, you would use a temporary variable like this:

x = 10
y = 20

print(f"x={x}, y={y}")  # x=10, y=20

tmp = x
x = y
y = tmp

print(f"x={x}, y={y}")  # x=20, y=10


# In Python, you can use the unpacking tuple syntax to achieve the same result:

x = 10
y = 20

print(f"x={x}, y={y}")  # x=10, y=20

# In this expression, Python evaluates the right-hand side first and then assigns the variable from the left-hand side to the values from the right-hand side.
x, y = y, x

print(f"x={x}, y={y}")  # x=20, y=10
