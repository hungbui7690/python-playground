"""
Iterables with different sizes

- If the iterables are of uneven size, and you want to fill missing values with a "fillvalue", you can use the zip_longest() function from the itertools module:

    itertools.zip_longest(*iterables, fillvalue=None)

"""

# By default, the fillvalue is None. For example:
from itertools import zip_longest

names = ("John", "Jane", "Alice", "Peter")
ages = (20, 22, 25)

for name, age in zip_longest(names, ages):
    print(name, age)

# John 20
# Jane 22
# Alice 25
# Peter None
