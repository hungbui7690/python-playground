"""
Using both *args and **kwargs arguments

"""


# The following function has both *args and **kwargs parameters:


def fn(*args, **kwargs):
    print(args)
    print(kwargs)


# The fn function can accept a variable number of the positional arguments. Python will pack them as a tuple and assign the tuple to the args argument.
# The fn function also accepts a variable number of keyword arguments. Python will pack them as a dictionary and assign the dictionary to the kwargs argument.


fn(1, 2, x=10, y=20)
# (1, 2)
# {'x': 10, 'y': 20}


"""
    Summary

        Use the Python **kwargs parameter to allow the function to accept a variable number of keyword arguments.
        Inside the function, the kwargs argument is a dictionary that contains all keyword arguments as its name-value pairs.
        Precede double stars (**) to a dictionary argument to pass it to **kwargs parameter.
        Always place the **kwargs parameter at the end of the parameter list, or you’ll get an error.

"""
