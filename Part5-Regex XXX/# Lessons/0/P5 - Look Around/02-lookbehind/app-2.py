"""
LOOKBEHIND

Negative lookbehind

- The negative lookbehind has the following syntax:

        (?<!Y)X

- This pattern matches X if there is no Y before it.

"""

import re


# The following example uses a negative lookbehind to match a number that doesn’t have the $ sign before it:
s = "1 phone costs $500"
pattern = r"\b(?<!\$)\d+\b"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.group())
# 1


"""
In the regular expression:

    r'\b(?<!\$)\d+\b'

        + The \b matches the word boundary.
        + The (?<!\$) is a negative lookbehind that does not match the $ sign.
        + The \d+ matches a number with one or more digits.

\\\\\\\\\\\\\\\

Summary

    A lookbehind (?<!Y)X matches X only if there is element Y before it.
    A negative lookbehind (?<!Y)X matches X only if there’s no element Y before it.
"""
