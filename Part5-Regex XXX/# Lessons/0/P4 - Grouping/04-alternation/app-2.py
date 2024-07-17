"""
REGEX ALTERNATION

1) Use Python regex alternation for matching time in hh:mm format

- To match a time string in the hh:mm format, you can combine the \d character set with the quantifiers {}:

        '\d{2}:\d{2}'

- In this pattern:

        \d{2} matches two digits.
        : matches the colon character.
        \d{2} matches two digits.

- However, the rule \d{2} also matches a number that is not a valid hour or minute, such as 99.

- To fix this, you can use the regex alternation.

- If the valid hour ranges from 01 to 23, you can use the following pattern to match the hour part:

        [01]\d|2[0-3]

- In this pattern:

        [01] matches a single digit 0 or 1
        \d matches a single digit from 0 to 9
        [01]\d matches 00, 01 to 19
        2 matches the digit 2
        [0-3] matches a single digit from 0 to 3 including 0, 1, 2, 3
        2[0-3] matches two digits 20, 21, 22, and 23.

- Therefore, the [01]\d|2[0-3] matches two digits from 00 to 23

- Because the valid minute ranges from 00 to 59, you can use the following pattern to match it:

        [0-5]\d

- The following regular expression combines the two rules above to match the time in the hh:mm format:

        '[01]\d|2[0-3]:[0-5]\d'

"""

import re


# However, this regular expression will not work as expected. For example:
s = "09:30 30:61 22:30 25:99"
pattern = r"[01]\d|2[0-3]:[0-5]\d"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())
# 09
# 22:30


# In this example, the regex engine treats pattern [01]\d|2[0-3]:[0-5]\d as two main parts separated by the alternation:
# [01]\d
# OR
# 2[0-3]):([0-5]\d)
