"""
CHARACTER SET

Introduction to Python regex character sets
- A character set (or a character class) is a set of characters, for example, digits (from 0 to 9), alphabets (from a to z), and whitespace.

- A character set allows you to construct regular expressions with patterns that match a string with one or more characters in a set.

        \d: digit character set

- Regular expressions use \d to represent a digit character set that matches a single digit from 0 to 9.

"""

# The following example uses the finditer() function to match every single digit in a string using the \d character set:

import re

s = "Python 3.0 was released in 2008"
matches = re.finditer("\d", s)
for match in matches:
    print(match.group())
# 3
# 0
# 2
# 0
# 0
# 8
