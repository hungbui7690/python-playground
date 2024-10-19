"""
ISALPHA
- The string isalpha() method returns True if:

    the string contains only alphabetic characters
    and the string has at least one character.

- Otherwise, the isalpha() method returns False.

- The following shows the syntax of the isalpha() method:

    str.isalpha()

*** Note that alphabetic characters are characters defined as letters in the Unicode character database.

"""

# The following example uses the isalpha() method to check if a string contains alphabetic characters:
name = "John"
print(name.isalpha())  # True
# It returned True because the string 'John' contains only alphabetic characters.


# The following example returns False because the string 'Jane Doe' contains a space:
name = "Jane Doe"
print(name.isalpha())  # False


# In general, if the string contains whitespace, the isalpha() method returns False.
# The following example uses the isalpha() method to check if all the characters in the string 'Python3' are alphabetic. It returns False because the string contains a number:
s = "Python3"
print(s.isalpha())  # False


# The following example returns False because the string is empty:
empty = ""
print(empty.isalpha())  # False
