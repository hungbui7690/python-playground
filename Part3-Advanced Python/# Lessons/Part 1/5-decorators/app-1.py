"""
What is a decorator in Python

- A decorator is a function that takes another function as an argument and extends its behavior without changing the original function explicitly.

"""


# The following defines a net_price function:


def net_price(price, tax):
    """calculate the net price from price and tax"""
    return price * (1 + tax)


# The net_price function calculates the net price from selling price and tax. It returns the net_price as a number.
# Suppose that you need to format the net price using the USD currency. For example, 100 becomes $100. To do it, you can use a decorator.


# By definition, a decorator is a function that takes a function as an argument and return another function:
def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"${result}"

    return wrapper


"""
The currency function returns the wrapper function. The wrapper function has the *args and **kwargs parameters.

These parameters allow you to call any fn function with any combination of positional and keyword-only arguments.

In this example, the wrapper function essentially executes the fn function directly and doesn’t change any behavior of the fn function.

The currency function is a decorator.

It accepts any function that returns a number and formats that number as a currency string.

To use the currency decorator, you need to pass the net_price function to it to get a new function and execute the new function as if it were the original function. For example:
"""

net_price = currency(net_price)
print(net_price(100, 0.05))  # $105.0
