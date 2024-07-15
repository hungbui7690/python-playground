"""
Backslash in f-strings

- PEP-498 specifies that an f-string cannot contain a backslash character as a part of the expression inside the curly braces {}.

"""

# 1. The following example will result in an error:
colors = ["red", "green", "blue"]
# s = f'The RGB colors are:\n {'\n'.join(colors)}'
# print(s)
# SyntaxError: f-string expression part cannot include a backslash


# 2. To fix this, you need to join the strings in the colors list before placing them in the curly braces:
colors = ["red", "green", "blue"]
rgb = "\n".join(colors)
s = f"The RGB colors are:\n{rgb}"
print(s)
# The RGB colors are:
# red
# green
# blue
