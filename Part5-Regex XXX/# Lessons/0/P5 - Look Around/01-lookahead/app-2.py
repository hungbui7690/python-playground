"""
LOOKAHEAD

Regex multiple lookaheads

- Regex allows you to have multiple lookaheads with the following syntax:

        X(?=Y)(?=Z)

- In this syntax, the regex engine will perform the following steps:

        Find X
        Test if Y is immediately after X, skip if it isn’t.
        Test if Z is also immediately after Y; skip if it isn’t.
        If both tests pass, the X is a match; otherwise, search for the next match.

- So the X(?=Y)(?=Z) pattern matches X followed by Y and Z simultaneously.
Regex negative lookaheads

- Suppose you want to match only the number 1 in the following text but not the number 4:

        '1 Python is about 4 feet long'

- To do that, you can use the negative lookahead syntax:

        X(?!Y)

"""

import re


# The X(?!Y) matches X only if it is not followed by Y. It’s the \d+ not followed by the literal string feet:
s = "1 Python is about 4 feet long"
pattern = "\d+(?!\s*feet)"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())
# 1


# Summary
# Use the Python regex lookahead X(?=Y) that matches X only if it is followed by Y.
# Use the negative regex lookahead X(?!Y) that matches X only if it is not followed by Y.
