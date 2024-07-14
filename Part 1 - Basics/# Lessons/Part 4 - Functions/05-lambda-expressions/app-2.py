"""
Lambda Expressions

"""


# 2) Functions that return a function example
# The following times() function returns a function which is a lambda expression:
def times(n):
    return lambda x: x * n


# And this example shows how to call the times() function:
double = times(2)


# Since the times() function returns a function, the double is also a function. To call it, you place parentheses like this:
result = double(2)
print(result)  # 4

result = double(3)
print(result)  # 6


# The following shows another example of using the times() function:
triple = times(3)

print(triple(2))  # 6
print(triple(3))  # 9
