"""
STRIP
- The string strip() method returns a copy of a string with the leading and trailing characters removed.

- The following shows the syntax of the strip() method:

    str.strip([chars])

- The strip() method has one optional argument.

- The chars argument is a string that specifies a set of characters which the strip() method will remove from the copy of the str.

- If you omit the chars argument or use None, the chars argument will default to whitespace characters. In other words, the strip() will remove leading and trailing whitespace characters from the str.

"""

# To get the whitespace characters, you can use the string module like this:

import string

print(string.whitespace)  # ' \t\n\r\x0b\x0c'


# 1) Using the strip() method to remove leading and trailing whitespace
# The following example uses the strip() method to return the copy of a string with the leading and trailing whitespace characters removed:
s = "\tHi, how are you?\n "
print(s)
new_s = s.strip()  #         Hi, how are you?
print(new_s)  # Hi, how are you?
# In this example, the string s contains a leading tab character and the trailing newline and space characters.
# Because we didn’t pass any argument to the strip() method, it returned a copy of the string s with all the leading and trailing whitespace characters removed.


# 2) Using the strip() method to remove leading and trailing characters
# The following example uses the strip() method to return a copy of a string with the leading and trailing characters . and # removed:
heading = "#.....Section 1.2.3 Bug #45....."
new_heading = heading.strip(".#")
print(new_heading)  # Section 1.2.3 Bug #45


# Summary

# Use the Python string strip(chars) method to return a copy of a string with the leading and trailing chars removed.
# Use the strip() method without argument to return a copy of a string with both leading and trailing whitespace characters removed.
