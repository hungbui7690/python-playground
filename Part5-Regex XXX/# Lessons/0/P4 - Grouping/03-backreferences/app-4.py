"""
BACKREFERENCES

2) Using Python regex backreferences to find words that have at least one consecutive repeated character

"""

import re


# The following example uses a backreference to find words that have at least one consecutive repeated character:
words = ["apple", "orange", "strawberry"]
pattern = r"\b\w*(\w)\1\w*\b"

results = [w for w in words if re.search(pattern, w)]

print(results)  # ['apple', 'strawberry']


# Summary
# Use a backreference \N to reference the capturing group N in a regular expression.
