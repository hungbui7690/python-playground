"""
Regex Quantifiers

- In regular expressions, quantifiers match the preceding characters or character sets a number of times. -
- The following table shows all the quantifiers and their meanings:

    Quantifier	Name	        Meaning
    *	        Asterisk	    Match its preceding element zero or more times.
    +	        Plus	        Match its preceding element one or more times.
    ?	        Question Mark	Match its preceding element zero or one time.
    { n }	    Curly Braces	Match its preceding element exactly n times.
    { n ,}	    Curly Braces	Match its preceding element at least n times.
    { n , m }	Curly Braces	Match its preceding element from n to m times.

"""


# Match zero or more times (*)

# The quantifier (*) matches its preceding element zero or more times. For example, the following program uses the * quantifier to match any string that ends with Python:

import re

s = """CPython, IronPython, and JPython 
       are major Python's implementation"""

matches = re.finditer("\w*Python", s)

for match in matches:
    print(match)

"""
In this example:

    The \w matches any single word character.
    So the \w* matches zero or more word characters.
    Therefore, the \w*Python match any zero or more characters followed by the string Python.

As a result, the \w*Python pattern matches CPython, IronPython, JPython, and Python in the string:

    <re.Match object; span=(0, 7), match='CPython'>
    <re.Match object; span=(9, 19), match='IronPython'>
    <re.Match object; span=(25, 32), match='JPython'>
    <re.Match object; span=(51, 57), match='Python'>
"""
