"""
FINDALL



"""

import re


# 3) Using the findall() function with a pattern that has multiple groups
# The following example uses the findall() functions to get tuples of strings that match the groups in the pattern:
s = "black, blue and brown"
pattern = r"(bl(\w+))"
matches = re.findall(pattern, s)

print(matches)  # [('black', 'ack'), ('blue', 'ue')]


# In this example, the pattern r'(bl(\w+))' has two capturing groups:
# (\w+) captures one or more word characters.
# # (bl(\w+)) captures the whole match.
