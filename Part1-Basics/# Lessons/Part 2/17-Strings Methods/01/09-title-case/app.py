"""
TITLE CASE

- The titlecase is a capitalization style used for titles so that the first letter of each word is uppercase and the remaining letters are lowercase. For example:

    Python Title Case Tutorial

- The rules for the titlecase, however, are not universally standardized.

- To make titlecased version of a string, you use the string title() method. The title() returns a copy of a string in the titlecase.

- The title() method converts the first character of each words to uppercase and the remaining characters in lowercase.

- The following shows the syntax of the title() method:

    str.title()

"""

# Regular Expression
import re


# The following example shows how to use the title() method to return the titlecased version of a string:
name = "john doe".title()
print(name)  # John Doe


# Python title() method limitation
# The title() method defines a word as a group of consecutive letters.
# This rule works in many contexts. However, it won’t work as you may expect if a string contains the apostrophes (‘) like contractions and possessives. For example:
s = "They're john's relatives.".title()
print(s)  # They'Re John'S Relatives.


# In this example, the string contains apostrophes (') that act as word boundaries. The title() method treats They're as two separate words.
# To fix it, you need to define a function that uses a regular expression:
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda word: word.group(0).capitalize(), s)


# And use the titlecase() function:
s = "They're john's relatives."
s = titlecase(s)
print(s)  # They're John's Relatives.
