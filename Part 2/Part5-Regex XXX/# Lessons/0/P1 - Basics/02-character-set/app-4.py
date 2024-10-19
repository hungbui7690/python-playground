"""
\s : whitespace character set

- The \s matches whitespace including a space, a tab, a newline, a carriage return, and a vertical tab.

"""

import re


# The following example uses the whitespace character set to match a space in a string:

s = "Python 3.0"
matches = re.finditer("\s", s)
for match in matches:
    print(match)
# <re.Match object; span=(6, 7), match=' '>
