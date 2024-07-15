"""
SWAPCASE
- The string swapcase() method returns a copy of a string with all lowercase characters converted to uppercase and vice versa.

- The following shows the syntax of the swapcase() method:

    str.swapcase()

- If you use English characters, the str.swapcase().swapcase() will be the same as str.

- However, it’s not always true for non-English characters. In other words, the following expression will not always be True:

    str.swapcase().swapcase() == str
"""

# The following example uses the string swapcase() method to return a copy of string with the letter case reversed:
message = "Hello"
new_message = message.swapcase()
print(new_message)  # hELLO


# The following example illustrate how to use the string swapcase() method with the non-English characters.
color = "weiß"
print(color)  # weiß

new_color = color.swapcase()
print(new_color)  # WEISS

print(color.swapcase().swapcase())  # weiss
print(color.swapcase().swapcase() == color)  # False

# The word 'weiß' is a German word. It means white in English. And the letter 'ß' is equivalent to 'ss'.
# The expression color.swapcase() returns 'WEISS'. So the expression color.swapcase().swapcase() returns 'weiss'.
# Therefore, expression color.swapcase().swapcase() == color returns False.


# Summary

# Use the Python string swapcase() method to return a copy of a string with all lowercase characters converted to uppercase and vice versa.
