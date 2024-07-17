"""
Match Exactly n Times: {n}

- The {n} quantifier matches its preceding element exactly n times, where n is zero or a positive integer.

"""


# For example, the following program uses the quantifier {n} to match a time string in the hh:mm format:

import re

s = "It was 11:05 AM"

matches = re.finditer("\d{2}:\d{2}", s)

for match in matches:
    print(match)

# <re.Match object; span=(7, 12), match='11:05'>


# In this example, the \d{2} matches exactly two digits. Therefore, the \d{2}:\d{2} matches a string that starts with two digits, a colon :, and ends with two digits.
