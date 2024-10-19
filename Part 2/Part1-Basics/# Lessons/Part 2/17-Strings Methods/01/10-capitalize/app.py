"""
CAPITALIZE

- The capitalize() is a built-in string method with the following syntax:

    str.capitalize()

- The capitalize() method takes no argument and returns a copy of the str with its first character capitalized and the other characters lowercased.

- The capitalize() makes the first character of a string uppercase, which works fine for ASCII. However, it won’t work for some non-English letters.

- For example, the letter NJ in Croatian appears as Nj at the start of words when the first character is uppercased:

    ǋemačka

- However, the capitalize() method returns the Ǌemačka:

    print('ǋemačka'.capitalize())

- To fix this issue, starting from Python 3.8, the capitalize() method puts the first character of the string into titlecase rather than uppercase.

- Note that to capitalize the first letter of every word in a string, you use the string title() method.

"""

# The following example shows how to use the capitalize() method to return a copy of a string with the first character converted to titlecase:

s = "now is better than never."
new_s = s.capitalize()
print(new_s)  # Now is better than never.


print("ǋemačka".capitalize())  # ǋemačka
