"""
CASEFOLD
- The Python string casefold() method returns a casefolded copy of the string.

- Casefolding is like case lowering. However, casefolding is more aggressive because it’s intended to remove all case distinctions in a string.

- If you use purely ASCII text, the lower() and casefold() methods return the same result.

- However, if you deal with Unicode characters, the casefold() method returns a more accurate result than the lower() method.

- For example, the letter 'ß' in Germany is equivalent to 'ss'. If you use the lower() method, the result would be 'ß' because the letter 'ß' is already lowercase.

- However, if you call the casefold() method on the string 'ß', it would return the 'ss' instead.

- For this reason, you should use the string casefold() method to carry case-insensitive string comparisons to achieve a more accurate result.

"""


# The following example illustrates how to use the lower() and casefold() methods to compare string case-insensitively:

color1 = "weiß"
color2 = "weiss"

print(color1 == color2)  # False
print(color1.lower() == color2.lower())  # False
print(color1.casefold() == color2.casefold())  # True
