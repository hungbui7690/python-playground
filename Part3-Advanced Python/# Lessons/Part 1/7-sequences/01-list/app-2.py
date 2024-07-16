"""
Standard Python sequence methods


"""

# 6) Concatenating two Python sequences
east = ["New York", "New Jersey"]
west = ["San Diego", "San Francisco"]

cities = east + west
print(cities)  # ['New York', 'New Jersey', 'San Diego', 'San Francisco']

# It’s quite safe to concatenate immutable sequences. The following example appends one element to the west list. And it doesn’t affect the cities sequence:
west.append("Sacramento")
print(west)  # ['San Diego', 'San Francisco', 'Sacramento']
print(cities)  # ['New York', 'New Jersey', 'San Diego', 'San Francisco']

# However, you should be aware of concatenations of mutable sequences. The following example shows how to concatenate a list to itself:
city = [["San Francisco", 900_000]]
cities = city + city
print(cities)  # [['San Francisco', 1000000], ['San Francisco', 1000000]]


# Since a list is mutable, the memory addresses of the first and second elements from the cities list are the same:
print(id(cities[0]) == id(cities[1]))  # True


# In addition, when you change the value from the original list, the combined list also changes:
city[0][1] = 1_000_000
print(cities)  # [['San Francisco', 1000000], ['San Francisco', 1000000]]


# 7) Repeating a Python sequence
s = "ha"
print(s * 3)  # hahaha
