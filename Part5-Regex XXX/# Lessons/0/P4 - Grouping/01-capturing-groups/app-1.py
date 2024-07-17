"""
CAPTURING GROUP

Introduction to the Python regex capturing groups

- Suppose you have the following path that shows the news with the id 100 on a website:

        news/100

- The following regular expression matches the above path:

        \w+/\d+

** Note that the above regular expression also matches any path that starts with one or more word characters, e.g., posts, todos, etc. not just news.

- In this pattern:

    - \w+ is a word character set with a quantifier (+) that matches one or more word characters.
    - / matches the forward slash / character.
    - \d+ is digit character set with a quantififer (+) that matches one or more digits.

"""


# The following program uses the \w+/\d+ pattern to match the string ‘news/100':

import re

s = "news/100"
pattern = "\w+/\d+"

matches = re.finditer(pattern, s)
for match in matches:
    print(match)

# <re.Match object; span=(0, 8), match='news/100'>


# It shows one match as expected.
# To get the id from the path, you use a capturing group. To define a capturing group for a pattern, you place the rule in parentheses:
# (rule)
