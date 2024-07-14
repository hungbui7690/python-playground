"""
Keyword Arguments


"""


# Let’s start with a simple function that calculates the net price from the selling price and discount:
def get_net_price(price, discount):
    return price * (1 - discount)


# The get_net_price() function has two parameters: price and discount.
# The following shows how to call the get_net_price() function to calculate the net price from the price 100 and discount 10%:
net_price = get_net_price(100, 0.1)
print(net_price)  # 90.0

# In the get_net_price(100, 0.1) function call, we pass each argument as a positional argument. In other words, we pass the price argument first and the discount argument second.
# However, the function call get_net_price(100, 0.1) has a readability issue. Because by looking at that function call only, you don’t know which argument is price and which one is the discount.
# On top of that, when you call the get_net_price() function, you need to know the position of each argument.
# If you don’t, the function will calculate the net_price incorrectly. For example:
net_price = get_net_price(0.1, 100)
print(net_price)  # -9.9

# To improve the readability, Python introduces the keyword arguments.
# The following shows the keyword argument syntax:
# fn(parameter1=value1,parameter2=value2)

# By using the keyword argument syntax, you don’t need to specify the arguments in the same order as defined in the function.
# Therefore, you can call a function by swapping the argument positions like this:
# fn(parameter2=value2,parameter1=value1)


# The following shows how to use the keyword argument syntax to call the get_net_price() function:
net_price = get_net_price(price=100, discount=0.1)

# Or:
net_price = get_net_price(discount=0.1, price=100)

# Both of them returns the same result.
# When you use the keyword arguments, their names that matter, not their positions.
# Note that you can call a function by mixing positional and keyword arguments. For example:
net_price = get_net_price(100, discount=0.1)
