"""
CAPTURING GROUP

"""

import re


# The lastindex property of the Match object returns the last index of all subgroups. The following program shows the entire match (group(0)) and all the subgroups:
s = "news/100"
pattern = "\w+/(\d+)"

matches = re.finditer(pattern, s)
for match in matches:
    for index in range(0, match.lastindex + 1):
        print(match.group(index))
# news/100
# 100

# In the output, the news/100 is the entire match while 100 is the subgroup.
