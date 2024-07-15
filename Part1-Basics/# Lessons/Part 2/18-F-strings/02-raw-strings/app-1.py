"""
Introduction to the Python raw strings

- In Python, when you prefix a string with the letter r or R such as r'...' and R'...', that string becomes a raw string. Unlike a regular string, a raw string treats the backslashes (\) as literal characters.

- Raw strings are useful when you deal with strings that have many backslashes, for example, regular expressions or directory paths on Windows.

"""

# To represent special characters such as tabs and newlines, Python uses the backslash (\) to signify the start of an escape sequence. For example:
s = "lang\tver\nPython\t3"
print(s)
# lang    ver
# Python  3


# However, raw strings treat the backslash (\) as a literal character. For example:
s = r"lang\tver\nPython\t3"
print(s)  # lang\tver\nPython\t3


# A raw string is like its regular string with the backslash (\) represented as double backslashes (\\):
s1 = r"lang\tver\nPython\t3"
s2 = "lang\\tver\\nPython\\t3"
print(s1 == s2)  # True


# In a regular string, Python counts an escape sequence as a single character:
s = "\n"
print(len(s))  # 1


# However, in a raw string, Python counts the backslash (\) as one character:
s = r"\n"
print(len(s))  # 2


# Since the backslash (\) escapes the single quote (') or double quotes ("), a raw string cannot end with an odd number of backslashes.
# For example:
# s = r'\' # SyntaxError: EOL while scanning string literal
# s = r'\\\' # SyntaxError: EOL while scanning string literal
