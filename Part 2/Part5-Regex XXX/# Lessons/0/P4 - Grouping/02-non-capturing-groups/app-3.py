"""
NON-CAPTURING GROUP


"""

import re


# To capture the minor version only, you can ignore the non-capturing group in the first place like this:
s = "Python 3.10"
pattern = "\d+\.(\d+)"
match = re.search(pattern, s)

# show the whole match
print(match.group())

# show the groups
for group in match.groups():
    print(group)

# 3.10
# 10


# So why do you use the non-capturing group anyway? the reason for using the non-capturing group is to save memory, as the regex engine doesn’t need to store the groups in the buffer.


# Summary
# Use the regex non-capturing group to create a group but don’t save it in the groups of the match.
