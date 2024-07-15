"""
ISTITLE
- The following show the syntax of the string istitle() method:

    str.istitle()

- The string istitle() method returns True if the string has at least one character and follows the title case rules. Otherwise, it returns False.

- Python uses very simple title case rules that the first character of each word in the string is uppercase while the remaining characters are lowercase.

- However, Python uses the apostrophe (‘) as word boundaries. Therefore, the following string is not title cased:

    "They're"

- However, the following string is title cased.

    "They'Re"

- This behavior is what you may not expect.

"""


# The following example uses the istitle() to check if a string follows the title case rules:

name = "Jane Doe"
is_title = name.istitle()
print(is_title)  # True


# However, the following example returns False because the string contains an apostrophe ('):

note = "Jane's Books"
is_title = note.istitle()
print(is_title)  # False
