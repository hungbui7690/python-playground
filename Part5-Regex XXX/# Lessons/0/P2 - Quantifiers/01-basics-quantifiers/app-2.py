"""
Match one or more times (+)

- The + quantifier matches its preceding element one or more times. For example, the \d+ matches one or more digits.

"""


# The following example uses the + quantifier to match one or more digits in a string:

import re

s = "Python 3.10 was released in 2021"

matches = re.finditer("\d+", s)

for match in matches:
    print(match)


# <re.Match object; span=(7, 8), match='3'>
# <re.Match object; span=(9, 11), match='10'>
# <re.Match object; span=(28, 32), match='2021'>
