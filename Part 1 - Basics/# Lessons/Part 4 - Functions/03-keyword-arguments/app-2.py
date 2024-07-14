"""
Keyword Arguments


"""


# Keyword arguments and default parameters
# Suppose that you have the following get_net_price() function that calculates the net price from the selling price, tax, and discount.
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)


# In the get_net_price() function, the tax and discount parameters have default values of 7% and 5% respectively.
# The following calls the get_net_price() function and uses the default values for tax and discount parameters:
net_price = get_net_price(100)
print(net_price)  # 102.0


# Suppose that you want to use the default value for the tax parameter but not discount. The following function call doesn’t work correctly.
net_price = get_net_price(100, 0.06)


# … because Python will assign 100 to price and 0.1 to tax, not discount.
# To fix this, you must use keyword arguments:
net_price = get_net_price(price=100, discount=0.06)
print(net_price)  # 101.0


# Or you can mix the positional and keyword arguments:
net_price = get_net_price(100, discount=0.06)
print(net_price)  # 101.0
