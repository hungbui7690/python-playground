"""
CAPTURING GROUP

"""

import re


# For example, to create a capturing group that captures the id from the path, you use the following pattern:
# '\w+/(\d+)'
# In this pattern, we place the rule \d+ inside the parentheses (). If you run the program with the new pattern, you’ll see that it displays one match:
s = "news/100"
pattern = "\w+/(\d+)"

matches = re.finditer(pattern, s)
for match in matches:
    print(match)

# <re.Match object; span=(0, 8), match='news/100'>


# To get the capturing groups from a match, you the group() method of the Match object:
# match.group(index)
# The group(0) will return the entire match while the group(1), group(2), etc., return the first, second, … group.
