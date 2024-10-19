"""
The dot(.) character set

- The dot (.) character set matches any single character except the new line (\n).

"""

import re

version = "Python\n4"
matches = re.finditer(".", version)
for match in matches:
    print(match.group())

# P
# y
# t
# h
# o
# n
# 4


"""
Summary
  Use \d character set to match any single digit.
  Use \w character set to match any single word character.
  Use \s character set to match any whitespace.
  The \D, \W, \S character set are the inverse sets of \d, \w, and \s character set.
  Use the dot character set (.) to match any character but a new line.
"""
