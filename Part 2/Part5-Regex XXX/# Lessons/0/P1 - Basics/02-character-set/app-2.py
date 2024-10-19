"""
CHARACTER SET


"""

import re


# To match a group of two digits, you use the \d\d. For example:

s = "Python 3.0 was released in 2008"
matches = re.finditer("\d\d", s)
for match in matches:
    print(match.group())
# 20
# 08


# Similarly, you can match a group of four digits using the \d\d\d\d pattern:

s = "Python 3.0 was released in 2008"
matches = re.finditer("\d\d\d\d", s)
for match in matches:
    print(match.group())
# 2008


# Later, you’ll learn how to use quantifiers to shorten the pattern. So instead of using the \d\d\d\d pattern, you can use the shorter one like \d{4}
