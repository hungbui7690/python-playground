"""
Introduction to Python dictionary comprehension

- A dictionary comprehension allows you to run a for loop on a dictionary and do something on each item like transforming or filtering and returns a new dictionary.

- Unlike a for loop, a dictionary comprehension offers a more expressive and concise syntax when you use it correctly.

- Here is the general syntax for dictionary comprehension:

      {key:value for (key,value) in dict.items() if condition}

- This dictionary comprehension expression returns a new dictionary whose item specified by the expression key: value

"""

# 1) Using Python dictionary comprehension to transform a dictionary
# Suppose that you have the following dictionary whose items are stock symbol and price:

stocks = {"AAPL": 121, "AMZN": 3380, "MSFT": 219, "BIIB": 280, "QDEL": 266, "LVGO": 144}

# To increase the price of each stock by 2%, you may come up with a for loop like this:
new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price * 1.02

print(new_stocks)
# {'AAPL': 123.42, 'AMZN': 3447.6, 'MSFT': 223.38, 'BIIB': 285.6, 'QDEL': 271.32, 'LVGO': 146.88}

"""
  How it works.

      First, loop over the items of the stocks dictionary
      Second, increase the price by 2% and add the item to the new dictionary (new_stocks).
"""


# The following example shows how to use dictionary comprehension to achieve the same result:

new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}
print(new_stocks)
