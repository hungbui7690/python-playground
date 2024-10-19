"""
REGEX GREEDY

- By default, all quantifiers work in a greedy mode. It means that the quantifiers will try to match their preceding elements as much as possible.


The unexpected result with greedy mode

- Suppose you have the following HTML fragment that represents a button element:

        s = '<button type="submit" class="btn">Send</button>'

- And you want to match the texts within the quotes ("") like submit and btn.
- To do that, you may come up with the following pattern that includes the quote (“), the dot (.) character set and the (+) quantifier:

        ".+"

- The meaning of the pattern is as follows:

    " starts with a quote
    . matches any character except the newline
    + matches the preceding character one or more times
    " ends with a quote

"""


# The following uses the finditer() function to match the string s with the pattern:

import re

s = '<button type="submit" class="btn">Send</button>'

pattern = '".+"'
matches = re.finditer(pattern, s)

for match in matches:
    print(match.group())

# "submit" class="btn"


# The result is not what you expected.
# By default, the quantifier (+) runs in the greedy mode, in which it tries to match the preceding element (".) as much as possible.
