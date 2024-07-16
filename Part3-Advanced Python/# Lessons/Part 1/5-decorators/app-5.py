"""
Decorator with Arguments

"""

from functools import wraps


# To define the repeat decorator, the repeat(5) should return the original decorator.
def repeat(times):
    """call a function a number of times"""

    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorate


# To fix this, you need to change the repeat decorator so that it accepts an argument that specifies the number of times a function should execute like this:
@repeat(10)
def say(message):
    """print the message
    Arguments
        message: the message to show
    """
    print(message)


say("Hi")

# In this code, the decorate function is a decorator. It’s equivalent to the original repeat decorator.
# Note that the new repeat function isn’t a decorator. It’s a decorator factory that returns a decorator.
