"""
Float to Int
- Suppose that you have a float such as 20.3, and you want to convert it to an integer.
- When you convert a float to an integer, you’ll have a data loss. For example, 20.3 may become 20 or 21.

- Python provides you with some functions in the math module for converting from a float to an int, including:

    Truncation
    Floor
    ceiling

"""


# Truncation
# The trunc(x) function returns the integer part of the number x. It ignores everything after the decimal point. For example:

from math import trunc

print(trunc(12.2))  # 12
print(trunc(12.5))  # 12
print(trunc(12.7))  # 12


# Similarly, the int() constructor accepts a float and uses truncation to cast a float to an int:

print(int(12.2))  # 12
print(int(12.5))  # 12
print(int(12.7))  # 12
