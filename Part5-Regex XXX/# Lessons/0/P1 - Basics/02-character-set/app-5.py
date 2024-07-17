"""
Inverse character sets

- A character set has an inverse character set that uses the same letter but in uppercase. The following table shows the character sets and their inverse ones:

        Character	  Inverse 	Description
        \d	        \D	      Match a single character except for a digit
        \w	        \W	      Match a single character that is not a word character
        \s	        \S	      Match a single character except for whitespace

"""

# The following example uses the \D to match the non-digit from a phone number:

import re

phone_no = "+1-(650)-513-0514"
matches = re.finditer("\D", phone_no)
for match in matches:
    print(match.group())

# +
# -
# (
# )
# -
# -
