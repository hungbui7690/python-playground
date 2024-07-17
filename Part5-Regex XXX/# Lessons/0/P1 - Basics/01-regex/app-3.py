"""
search() function

"""

# The search() function searches for a pattern within a string. If there is a match, it returns the first Match object or None otherwise. For example:

import re

s = "Python 3.10 was released on October 04, 2021."

pattern = "\d{2}"
match = re.search(pattern, s)
print(type(match))  # <class 're.Match'>
print(match)  # <re.Match object; span=(9, 11), match='10'>

# In this example, the search() function returns the first two digits in the string s as the Match object.


"""
Match object

- The Match object provides the information about the matched string. It has the following important methods:

    Method	    Description
    group()	    Return the matched string
    start()	    Return the starting position of the match
    end()	      Return the ending position of the match
    span()	    Return a tuple (start, end) that specifies the positions of the match

"""


s = "Python 3.10 was released on October 04, 2021."
result = re.search("\d", s)

print("Matched string:", result.group())
print("Starting position:", result.start())
print("Ending position:", result.end())
print("Positions:", result.span())

"""
Matched string: 3
Starting position: 7
Ending position: 8
Positions: (7, 8)
"""
