"""
REGEX SETS & RANGES

- Several characters or character sets inside square brackets [] mean matching for any character or character set among them.

\\\\\\\\\\\\\\\\\\\

Sets

- For example, [abc] means any of three characters. 'a', 'b', or 'c'. The [abc] is called a set. And you can use the set with regular characters to construct a search pattern.

"""


# For example, the following program uses the pattern licen[cs]e that matches both license and licence:

import re

s = "A licence or license"

pattern = "licen[cs]e"
matches = re.finditer(pattern, s)

for match in matches:
    print(match.group())
# licence
# license


"""
The pattern licen[cs]e searches for:

    licen
    then one of the letters [cs]
    then e.

Therefore, it matches license and licence.
"""
