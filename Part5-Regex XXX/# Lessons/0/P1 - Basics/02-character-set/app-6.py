"""
Inverse character sets

        Character	  Inverse 	Description
        \d	        \D	      Match a single character except for a digit
        \w	        \W	      Match a single character that is not a word character
        \s	        \S	      Match a single character except for whitespace

"""

# To turn the phone number +1-(650)-513-0514 into the 16505130514, you can use the sub() function:

import re


phone_no = re.sub("\D", "", "+1-(650)-513-0514")
print(phone_no)  # 16505130514


# In this example, the sub() function replaces the character that matches the pattern \D with the literal string '' in the formatted phone number.
