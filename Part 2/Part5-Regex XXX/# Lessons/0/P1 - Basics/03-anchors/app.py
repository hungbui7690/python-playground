"""
Introduction to the regex anchors

- Regular expressions provide you with two anchors that match the positions of characters:

    ^ – the caret anchor matches at the beginning of a string.
    $ – the dollar anchor matches at the end of a string.

"""

import re


# The following example uses the \d\d to match two digits in a time string:
time = "12:20"
matches = re.finditer("\d\d", time)
for match in matches:
    print(match.group())
# 12
# 20


# If you use the caret anchor (^), you’ll get one group which is the two digits at the beginning of the string. For example:
time = "12:20"
matches = re.finditer("^\d\d", time)
for match in matches:
    print(match.group())
# 12


# Similarly, if you use the $ anchor, you’ll get the last two digits because the $ matches \d\d at the end of the time string:
time = "12:20"
matches = re.finditer("\d\d$", time)
for match in matches:
    print(match.group())
# 20


# To check if a string is a time string, you can combine the caret (^) and dollar ($) anchors. For example:
time = "12:20"
matches = re.finditer("^\d\d:\d\d$", time)
for match in matches:
    print(match.group())
# 12:20


# Note that the pattern ^\d\d:\d\d$ doesn’t validate the valid hour and minute. For example, it also matches the following string:
# 30:99
# It’s not a valid time string because the valid hour is from 1 to 24 and the valid minute is from 00 to 59. Later, you’ll learn how to match the time string with valid values using the alternation.


# Summary
# Regex anchors match character positions, not the characters.
# The caret anchor (^) matches at the beginning of a string.
# The dollar anchor ($) matches at the end of a string.
