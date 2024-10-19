"""
\w: the word character set

- Regular expressions use \w to represent the word character set. The \w matches a single ASCII character including Latin alphabet, digit, and underscore (_).


"""

import re


# The following example uses the finditer() function to match every single word character in a string using the \w character set:

s = "Python 3.0"
matches = re.finditer("\w", s)
for match in matches:
    print(match.group())
# P
# y
# t
# h
# o
# n
# 3
# 0


# Notice that the whitespace and . are not included in the matches.
