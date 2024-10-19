"""
Decorator with Arguments
- Suppose that you have a function called say that prints out a message:
- ...and you want to execute the say() function 5 times repeatedly each time you call it. For example:

"""

from functools import wraps


# And you can define the repeat decorator as follows:
def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result

    return wrapper


# To do that, you can use a regular decorator:
@repeat
def say(message):
    """print the message
    Arguments
        message: the message to show
    """
    print(message)


say("Hi")


"""
What if you want to execute the say() function repeatedly ten times. In this case, you need to change the hard-coded value 5 in the repeat decorator.

However, this solution isn’t flexible. For example, you want to use the repeat decorator to execute a function 5 times and another 10 times. The repeat decorator would not meet the requirement.
"""
