"""
REGEX ALTERNATION

- To represent an alternation in regular expressions, you use the pipe operator (|). The pipe operator is called the alternation. It is like the or operator in Python.

- The following regular expression uses an alternation to match either the literal string complex and simple:

        'simple|complex'

"""

import re


# For example, the following program uses the above regular expression to match either the literal string simple or complex:
s = "simple is better than complex"
pattern = r"simple|complex"

matches = re.findall(pattern, s)
print(matches)  # ['simple', 'complex']
