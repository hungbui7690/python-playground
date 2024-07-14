"""
Numbers

"""

# Floats
# Any number with a decimal point is a floating-point number. The term float means that the decimal point can appear at any position in a number.
# In general, you can use floats like integers. For example:
print(0.5 + 0.5)
print(0.5 - 0.5)
print(0.5 * 0.5)
print(0.5 / 0.5)

# The division of two integers always returns a float:
print(20 / 10)  # 2.0

# If you mix an integer and a float in any arithmetic operation, the result is a float:
print(1 + 2.0)

# Due to the internal representation of floats, Python will try to represent the result as precisely as possible. However, you may get the result that you would not expect. For example:
print(0.1 + 0.2)  # 0.30000000000000004
# Just keep this in mind when you perform calculations with floats. And you’ll learn how to handle situations like this in later tutorials.
