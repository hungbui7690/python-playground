"""
Match from n and m times: {n,m}

- The {n,m} quantifier matches its preceding element at least n times, but no more than m times, where n and m are zero or a positive integer.

"""

import re

s = "5-5-2021 or 05-05-2021 or 5/5/2021"

matches = re.finditer("\d{1,2}-\d{1,2}-\d{4}", s)

for match in matches:
    print(match)


# <re.Match object; span=(0, 8), match='5-5-2021'>
# <re.Match object; span=(12, 22), match='05-05-2021'>


# In this example, the pattern \d{1,2} matches one or two digits. So the pattern \d{1,2}-\d{1,2}-\d{4} matches a date string in the d-m-yyyy or dd-mm-yyyy format.


# Summary
# Quantifiers match their preceding elements a number of times.
