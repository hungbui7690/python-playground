"""
Introspecting decorated functions

- When you decorate a function:

    @decorate
    def fn(*args,**kwargs):
        pass

- It’s equivalent:

    fn = decorate(fn)

- The decorate function returns a new function, which is the wrapper function.

"""

from functools import wraps


# 3. when we at @, it will show the documentation with the "help method"
def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"${result}"

    return wrapper


@currency
def net_price(price, tax):
    """calculate the price based on tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


print(net_price(100, 0.05))  # $105.0


# 1. If you use the built-in help function to show the documentation of the new function, you won’t see the documentation of the original function. For example:
help(net_price)  # wrapper(*args, **kwargs)


# 2. Also, if you check the name of the new function, Python will return the name of the inner function returned by the decorator:
print(net_price.__name__)  # wrapper
# So when you decorate a function, you’ll lose the original function signature and documentation.
# To fix this, you can use the wraps function from the functools standard module. In fact, the wraps function is also a decorator.


# Summary
# A decorator is a function that changes the behavior of another function without explicitly modifying it.
# Use the @ symbol to decorate a function.
# Use the wraps function from the functools built-in module to retain the documentation and name of the original function.
