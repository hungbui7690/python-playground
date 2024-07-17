"""
CAPTURING GROUP

"""

import re


# If you want to capture also the resource (news) in the path (news/100), you can create an additional capturing group like this:
# '(\w+)/(\d+)'
s = "news/100"
pattern = "(\w+)/(\d+)"

matches = re.finditer(pattern, s)
for match in matches:
    for index in range(0, match.lastindex + 1):
        print(match.group(index))
# news/100
# news
# 100


# In the output, the news/100 is the entire match while news and 100 are the subgroups.
