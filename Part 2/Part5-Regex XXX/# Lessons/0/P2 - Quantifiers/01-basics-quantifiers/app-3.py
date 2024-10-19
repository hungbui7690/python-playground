"""
Match zero or one time (?)

- The ? quantifier matches its preceding element zero or one time.

"""


# The following example uses the (?) quantifier to match both strings color and colour:

import re

s = "What color / colour do you like?"

matches = re.finditer("colou?r", s)

for match in matches:
    print(match)


# <re.Match object; span=(5, 10), match='color'>
# <re.Match object; span=(13, 19), match='colour'>


# In this example, the u? matches zero or one character u. Therefore, the colou?r pattern matches both color and colour
