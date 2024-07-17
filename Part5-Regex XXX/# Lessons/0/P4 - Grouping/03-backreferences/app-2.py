"""
BACKREFERENCES

1) Using Python regex backreferences to get text inside quotes

    - Suppose you want to get the text within double quotes:

            "This is regex backreference example"

    - Or single quote:

            'This is regex backreference example'

    - But not mixed of single and double-quotes. The following will not match:

            'not match"

    - To do this, you may use the following pattern:

            '[\'"](.*?)[\'"]'
"""

import re


# However, this pattern will match text that starts with a single quote (‘) and ends with a double quote (“) or vice versa. For example:
s = '"Python\'s awesome". She said'
pattern = "['\"].*?['\"]"

match = re.search(pattern, s)

print(match.group(0))  # "Python'
