"""
RSTRIP
- The rstrip() method returns a copy of a string with the trailing characters removed.

- The following shows the syntax of the rstrip() method:

    str.rstrip([chars])

- The rstrip() method has one optional argument chars.

- The chars argument is a string that specifies a set of characters which the rstrip() method will remove from the copy of the str.

- If you omit the chars argument or use None, the chars argument defaults to whitespace characters. In this case, the rstrip() method will remove the trailing whitespace characters from the copy of the str.

- The following are whitespace characters in Python:

    ' ' – the space character
    \t – the tab character
    \n – the newline or linefeed character
    \r – the carriage return
    \x0b – the vertical tab. It can be also expressed as \v.
    \x0c – the form feed character that forces a printer to move the next sheet of paper. It’s also expressed as \f.

"""

# 1) Using the rstrip() method to remove the trailing whitespace characters
# The following example illustrates how to use the rstrip() method to return a copy of a string with the trailing whitespace characters removed:
s = "Now is better than never. \n"
print(s)
new_s = s.rstrip()
print(new_s)
# In this example, the string s contains a trailing space and a newline character.
# Because we didn’t pass any argument to the rstrip() method, it returned a copy of the string s with all the trailing whitespace characters removed.


# 2) Using the rstrip() method to remove the trailing characters
# The following example uses the rstrip() method to return a copy of a string with trailing characters . and # removed:
heading = "Section 1. Issue #15....."
new_heading = heading.rstrip(".#")
print(new_heading)  # Section 1. Issue #15


# Summary

# Use the Python string rstrip(chars) method to return a copy of a string with the trailing characters removed.
# Use the rstrip() method without argument to return a copy of a string with the trailing whitespace removed.
