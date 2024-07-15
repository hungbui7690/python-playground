"""
Introduction to the Python **kwargs parameters

"""


# If a function has the **kwargs parameter and other parameters, you need to place the **kwargs after other parameters. Otherwise, you’ll get an error.

# The syntax of the following connect() function is correct:


def connect(fn, **kwargs):
    print(kwargs)


# However, the syntax of this function causes a SyntaxError:
# def connect(**kwargs, fn):
#     print(kwargs)
