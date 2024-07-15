"""
Python partial function from functools module

- The following shows the syntax of the partial function from the functools module:

    functools.partial(fn, /, *args, **kwargs)

- The partial function returns new partial object, which is a callable.

- When you call the partial object, Python calls the fn function with the positional arguments args and keyword arguments kwargs.

"""


# The following example shows how to use the partial function to define the double function from the multiply function:

from functools import partial


def multiply(a, b):
    return a * b


double = partial(multiply, b=2)

result = double(10)
print(result)  # 20


"""
    How it works.

        First, import the partial function from the functools module.
        Second, define the multiply function.
        Third, return a partial object from the partial function and assign it to the double variable.

    When you call the double, Python calls the multiply function where b argument defaults to 2.

    If you pass more arguments to a partial object, Python appends them to the args argument.

    When you pass additional keyword arguments to a partial object, Python extends and overrides the kwargs arguments.

"""


# Therefore, it’s possible to call the double like this:
double(10, b=3)  # 30

# In this example, Python will call the multiply function where the value of the b argument is 3, not 2.
