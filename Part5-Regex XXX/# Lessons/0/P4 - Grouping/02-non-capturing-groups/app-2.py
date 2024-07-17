"""
NON-CAPTURING GROUP


"""

import re


# Suppose you don’t want to capture the digits before the literal character (.), you can use a non-capturing group like this:
s = "Python 3.10"
pattern = "(?:\d+)\.(\d+)"

match = re.search(pattern, s)

# show the whole match
print(match.group())

# show the groups
for group in match.groups():
    print(group)

# 3.10
# 10


# In this example, we use the non-capturing group for the first group:
# (?:\d+)
