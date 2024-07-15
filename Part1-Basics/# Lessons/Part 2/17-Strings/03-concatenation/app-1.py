"""
7 Ways to Concatenate Strings in Python
- Python provides you with various ways to concatenate one or more strings into a new string.
- Since Python string is immutable, the concatenation always results in a new string.

"""

# 1) Concatenating literal strings
# To concatenate two or more literal strings, you just need to place them next to each other. For example:
s = "String" " Concatenation"
print(s)
# Note that this way won’t work for the string variables.


# 2) Concatenating strings using the + operator
# A straightforward way to concatenate multiple strings into one is to use the + operator:
s = "String" + " Concatenation"
print(s)


# And the + operator works for both literal strings and string variables. For example:
s1 = "String"
s2 = s1 + " Concatenation"
print(s2)
