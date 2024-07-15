"""
Python partial functions and variables

"""


# Sometimes, you may want to use variables for creating partials. For example:

from functools import partial


def multiply(a, b):
    return a * b


x = 2
f = partial(multiply, x)

result = f(10)  # 20
print(result)

x = 3
result = f(10)  # 20
print(result)


"""
    In this example, we change x to 3 and expect that f(10) would return 30 instead of 20.

    However, f(10) returns 20 instead. It’s because Python evaluates the value of x in the following statement:

        f = partial(multiply, x)

    …but not after that, therefore, when x references to the new number (3), the partial function doesn’t change.
"""
