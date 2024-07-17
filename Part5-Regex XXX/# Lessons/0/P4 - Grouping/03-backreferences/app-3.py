"""
BACKREFERENCES

- To fix it, you can use a backreference:

        r'([\'"]).*?\1'

- The backreference \1 refers to the first capturing group. So if the subgroup starts with a single quote, the \1 will match the single quote. And if the subgroup starts with a double-quote, the \1 will match the double-quote.

"""

import re


s = '"Python\'s awesome". She said'
pattern = r'([\'"])(.*?)\1'

match = re.search(pattern, s)
print(match.group())  # "Python's awesome"
