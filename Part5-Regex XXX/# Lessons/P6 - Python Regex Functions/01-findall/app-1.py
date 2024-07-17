"""
FINDALL

Introduction to the Python regex findall() function

- The findall() is a built-in function in the re module that handles regular expressions. The findall() function has the following syntax:

        re.findall(pattern, string, flags=0)

- In this syntax:

        pattern is a regular expression that you want to match.
        string is the input string
        flags is one or more regular expression flags that modify the standard behavior of the pattern.

- The findall() function scans the string from left to right and finds all the matches of the pattern in the string.

- The result of the findall() function depends on the pattern:

        If the pattern has no capturing groups, the findall() function returns a list of strings that match the whole pattern.
        If the pattern has one capturing group, the findall() function returns a list of strings that match the group.
        If the pattern has multiple capturing groups, the findall() function returns the tuples of strings that match the groups.

- It’s important to note that the non-capturing groups do not affect the form of the return result.

"""

import re


# 1) Using the Python regex findall() to get a list of matched strings
# The following example uses the findall() function to get a list of color names that start with the literal string bl:
s = "black, blue and brown"
pattern = r"bl\w+"
matches = re.findall(pattern, s)

print(matches)  # ['black', 'blue']


# The following pattern matches a literal string bl followed by one or more word characters specified by the \w+ rule:
# 'bl\w+'
# Therefore, the findall() function returns a list of strings that match the whole pattern.
