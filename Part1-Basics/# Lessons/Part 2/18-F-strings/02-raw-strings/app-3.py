"""
Raw Strings

"""

# 1. Convert a regular string into a raw string
# To convert a regular string into a raw string, you use the built-in repr() function. For example:
s = "\n"
raw_string = repr(s)

print(raw_string)  # '\n'


# 2. Note that the result raw string has the quote at the beginning and end of the string. To remove them, you can use slices:
s = "\n"
raw_string = repr(s)[1:-1]
print(raw_string)  # \n


# Summary

# Prefix a literal string with the letter r or R to turn it into a raw string.
# Raw strings treat backslash as a literal character.
