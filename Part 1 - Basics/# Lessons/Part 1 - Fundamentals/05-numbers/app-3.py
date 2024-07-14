"""
Numbers
- Python supports integers, floats, and complex numbers. This tutorial discusses only integers and floats.

"""

# Underscores in numbers
# When a number is large, it’ll become difficult to read. For example:
count = 10000000000

# To make the long numbers more readable, you can group digits using underscores, like this:
count = 10_000_000_000

# When storing these values, Python just ignores the underscores. It does so when displaying the numbers with underscores on the screen:
count = 10_000_000_000
print(count)  # 10000000000


# The underscores also work for both integers and floats.
# Note that the underscores in numbers have been available since Python 3.6
