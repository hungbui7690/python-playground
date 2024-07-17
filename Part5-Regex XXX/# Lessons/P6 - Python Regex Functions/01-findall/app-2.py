"""
FINDALL



"""

import re


# 2) Using the findall() function with a pattern that has a single group
# The following example uses the findall() function to get a list of strings that match a group:
s = "black, blue and brown"
pattern = r"bl(\w+)"
matches = re.findall(pattern, s)

print(matches)  # ['ack', 'ue']

# This example uses the regular expression r'bl(\w+)' that has one capturing group (\w+). Therefore, the findall() function returns a list of strings that match the group.
