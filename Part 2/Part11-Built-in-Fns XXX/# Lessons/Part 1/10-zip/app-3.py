"""
Iterables with different sizes

- The iterables passed to the zip() function may have different sizes. The zip() has three different strategies to deal with this issue.

"""

# By default, the zip() will stop when it completes iterating the shortest iterable. It’ll ignore the remaining items in the longer iterables. For example:
names = ("John", "Jane", "Alice", "Peter")
ages = (20, 22, 25)

for name, age in zip(names, ages):
    print(name, age)

# John 20
# Jane 22
# Alice 25


# In this example, the zip() function performs three iterations based on the shortest size of the names and ages.
# If you want to ensure that the iterables must have the same sizes, you can use the strict=True option. In this case, if the sizes of the iterables are different, the zip() will raise a ValueError.
# Note that the strict argument has been available since Python 3.10


# For example, the following will raise a ValueError exception because the sizes of the iterables are different:
names = ("John", "Jane", "Alice", "Peter")
ages = (20, 22, 25)

for name, age in zip(names, ages, strict=True):  # ValueError 🛑
    print(name, age)

# ValueError: zip() argument 2 is shorter than argument 1
