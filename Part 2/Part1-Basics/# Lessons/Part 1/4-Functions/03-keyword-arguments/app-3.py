"""
Keyword Arguments


"""


def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)


# Python keyword argument requirements
# Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.
# The following will result in an error because it uses the positional argument after a keyword argument:
# net_price = get_net_price(100, tax=0.08, 0.06) # SyntaxError: positional argument follows keyword argument


# To fix this, you need to use the keyword argument for the third argument like this:
net_price = get_net_price(100, tax=0.08, discount=0.06)
print(net_price)


"""
    Summary

        Use the Python keyword arguments to make your function call more readable and obvious, especially for functions that accept many arguments.
        All the arguments after the first keyword argument must also be keyword arguments too.

"""
