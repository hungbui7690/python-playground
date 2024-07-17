"""
REGEX ALTERNATION

- To fix it, you need to wrap the alternation inside parentheses to indicate that only that part is alternated, not the whole expression like this:

        ([01]\d|2[0-3]):[0-5]\d

"""

import re


# Now, the program works as expected:
s = "09:30 30:61 22:30 25:99"
pattern = r"([01]\d|2[0-3]):[0-5]\d"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())
# 09:30
# 22:30


# Summary
# The regex alternation X | Y matches either X or Y.
# The regex alternation is like an OR operator in regular expressions.
# Place the alternation part inside parentheses () to express that only that part is alternated.
