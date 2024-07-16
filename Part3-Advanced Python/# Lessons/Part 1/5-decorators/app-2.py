"""
Python decorator definition

- In general, a decorator is:

    A function that takes another function (original function) as an argument and returns another function (or closure)
    The closure typically accepts any combination of positional and keyword-only arguments.
    The closure function calls the original function using the arguments passed to the closure and returns the result of the function.

- The inner function is a closure because it references the fn argument from its enclosing scope or the decorator function.

"""


def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"${result}"

    return wrapper


"""
1. The @ symbol

- In the previous example, the currency is a decorator. And you can decorate the net_price function using the following syntax:

    net_price = currency(net_price)

- Generally, if decorate is a decorator function and you want to decorate another function fn, you can use this syntax:

    fn = decorate(fn)

2. To make it more convenient, Python provides a shorter way like this:

    @decorate
    def fn():
        pass

3. For example, instead of using the following syntax:

    net_price = currency(net_price)

"""


# 4. … you can decorate the net_price function using the @currency as follows:
@currency
def net_price(price, tax):
    """calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


# 5.
print(net_price(100, 0.05))  # $105.0
