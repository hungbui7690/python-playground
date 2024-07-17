"""
match() function

"""

# The match() function returns a Match object if it finds a pattern at the beginning of a string. For example:

import re

items = [
    "Python",
    "CPython is an implementation of Python written in C",
    "Jython is a Java implementation of Python",
    "IronPython is Python on .NET framework",
]

pattern = "\wython"

for s in items:
    result = re.match(pattern, s)
    print(result)

"""
<re.Match object; span=(0, 6), match='Python'>
None
<re.Match object; span=(0, 6), match='Jython'>
None
"""


"""
In this example, the \w is the word character set that matches any single character.

The \wython matches any string that starts with any sing word character and is followed by the literal string ython, for example, Python.

Since the match() function only finds the pattern at the beginning of a string, the following strings match the pattern:

    Python
    Jython is a Java implementation of Python

And the following string doesn’t match:

    'CPython is an implementation of Python written in C'
    'IronPython is Python on .NET framework'

"""
