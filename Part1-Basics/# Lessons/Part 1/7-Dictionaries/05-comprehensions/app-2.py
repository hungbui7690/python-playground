"""
Dictionary Comprehension
- A dictionary comprehension iterates over items of a dictionary and allows you to create a new dictionary by transforming or filtering each item.

"""

# 2) Using Python dictionary comprehension to filter a dictionary
# To select stocks whose prices are greater than 200, you may use the following for loop:

stocks = {"AAPL": 121, "AMZN": 3380, "MSFT": 219, "BIIB": 280, "QDEL": 266, "LVGO": 144}

selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

print(selected_stocks)  # {'AMZN': 3380, 'MSFT': 219, 'BIIB': 280, 'QDEL': 266}


# The following example uses the dictionary comprehension with an if clause to get the same result:

selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}
print(selected_stocks)  # {'AMZN': 3380, 'MSFT': 219, 'BIIB': 280, 'QDEL': 266}
