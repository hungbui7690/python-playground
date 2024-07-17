"""
FINDALL



"""

import re


# 4) Using the findall() function with a regular expression flag
# The following example uses the findall() function with the re.IGNORECASE flag:
s = "Black, blue and brown"
pattern = r"(bl(\w+))"
matches = re.findall(pattern, s, re.IGNORECASE)

print(matches)  # [('Black', 'ack'), ('blue', 'ue')]


# In this example, we use the re.IGNORECASE flag in the findall() function that ignores the character cases of the matched strings. Therefore, the output includes both Black and blue.


# Summary
# Use the Python regex findall() function to get a list of matched strings.
