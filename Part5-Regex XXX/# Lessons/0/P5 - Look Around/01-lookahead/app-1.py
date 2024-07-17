"""
LOOKAHEAD

- Sometimes, you want to match X but only if it is followed by Y. In this case, you can use the lookahead in regular expressions.

- The syntax of the lookahead is as follows:

        X(?=Y)

- This syntax means to search for X but matches only if it is followed by Y.

- For example, suppose you have the following string:

        '1 Python is about 4 feet long'

- And you want to match the number (4) that is followed by a space and the literal string feet, not the number 1. In this case, you can use the following pattern that contains a lookahead:

        \d+(?=\s*feet)

- In this pattern:

        + \d+ is the combination of the digit character set with the + quantifier that matches one or more digits.
        + ?= is the lookahead syntax
        + \s* is the combination of the whitespace character set and * quantifier that matches zero or more whitespaces.
        + feet matches the literal string feet.

"""

import re


# The following code uses the above pattern to match the number that is followed by zero or more spaces and the literal string feet:
s = "1 Python is about 4 feet long"
pattern = "\d+(?=\s*feet)"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())

# 4
