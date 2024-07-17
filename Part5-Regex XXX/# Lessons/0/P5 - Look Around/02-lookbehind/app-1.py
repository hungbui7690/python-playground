"""
LOOKBEHIND

- In regular expressions, the lookbehind matches an element if there is another specific element before it. The lookbehind has the following syntax:

        (?<=Y)X

- In this syntax, the pattern will match X if there is Y before it.

- For example, suppose you have the following string and want to match the number 500 not the number 1:

        '1 phone costs $500'

- To do that, you can use the following regular expression with a lookahead like this:

        (?<=\$)\d+

- In this pattern:

        - (?<=\$) matches an element if there is a literal string $ before it. Since the $ is a special character in the regex, we use the backslash character \ to escape it. As a result, the regex engine will treat \$ as a regular character $.
        - \d+ matches one or more digits.

"""

import re


# The following example uses a regular expression with a lookbehind to match a number that has the $ sign before it:
s = "1 phone costs $500"
pattern = "(?<=\$)\d+"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())
# 500
