"""
fullmatch() function

"""

# The fullmatch() function returns a Match object if the whole string matches a pattern or None otherwise. The following example uses the fullmatch() function to match a string with four digits:

import re

s = "2021"
pattern = "\d{4}"
result = re.fullmatch(pattern, s)
print(result)

# <re.Match object; span=(0, 4), match='2021'>


# The pattern '\d{4}' matches a string with four digits. Therefore, the fullmatch() function returns the string 2021.


# If you place the number 2021 at the middle or the end of the string, the fullmatch() will return None. For example:
s = "Python 3.10 released in 2021"
pattern = "\d{4}"
result = re.fullmatch(pattern, s)
print(result)  # None
