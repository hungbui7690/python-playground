"""
Match at least n times: {n,}

- The {n,} quantifier matches its preceding element at least n times, where n is zero or a positive integer.

"""


# For example, the following program uses the {n, } quantifier to match the date strings with the m-d-yyyy or mm-dd-yyyy format:

import re

s = "5-5-2021 or 05-05-2021 or 5/5/2021"

matches = re.finditer("\d{1,}-\d{1,}-\d{4}", s)

for match in matches:
    print(match)


# <re.Match object; span=(0, 8), match='5-5-2021'>
# <re.Match object; span=(12, 22), match='05-05-2021'>
