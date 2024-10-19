"""
Filter List Elements

"""

# Using the Python filter() function to filter a list of tuples example
# Suppose you have the following list of tuples:

countries = [
    ["China", 1394015977],
    ["United States", 329877505],
    ["India", 1326093247],
    ["Indonesia", 267026366],
    ["Bangladesh", 162650853],
    ["Pakistan", 233500636],
    ["Nigeria", 214028302],
    ["Brazil", 21171597],
    ["Russia", 141722205],
    ["Mexico", 128649565],
]

# Each element in a list is a tuple that contains the country’s name and population.
# To get all the countries whose populations are greater than 300 million, you can use the filter() function as follows:
populated = filter(lambda c: c[1] > 300_000_000, countries)
print(
    list(populated)
)  # [['China', 1394015977], ['United States', 329877505], ['India', 1326093247]]
