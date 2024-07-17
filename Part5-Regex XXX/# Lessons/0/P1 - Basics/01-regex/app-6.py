"""
Regular expressions and raw strings

- It’s important to note that Python and regular expression are different programming languages. They have their own syntaxes.
- The re module is the interface between Python and regular expression programming languages. It behaves like an interpreter between them.
- To construct a pattern, regular expressions often use a backslash '\' for example \d and \w . But this collides with Python’s usage of the backslash for the same purpose in string literals.


- For example, suppose you need to match the following string:

        s = '\section'

- In Python, the backslash (\) is a special character. To construct a regular expression, you need to escape any backslashes by preceding each of them with a backslash (\):

        pattern = '\\section'

- In regular expressions, the pattern must be '\\section'. However, to express this pattern in a string literal in Python, you need to use two more backslashes to escape both backslashes again:

        pattern = '\\\\section'

- Simply put, to match a literal backslash ('\'), you have to write '\\\\' because the regular expression must be '\\' and each backslash must be expressed as '\\' inside a string literal in Python.
- This results in lots of repeated backslashes. Hence, it makes the regular expressions difficult to read and understand.
- A solution is to use the raw strings in Python for regular expressions because raw strings treat the backslash (\) as a literal character, not a special character.

"""

# To turn a regular string into a raw string, you prefix it with the letter r or R. For example:

import re

s = "\section"
pattern = r"\\section"
result = re.findall(pattern, s)

print(result)  # ['\\section']


# Note that in Python ‘\section’ and ‘\\section’ are the same:
p1 = "\\section"
p2 = "\section"
print(p1 == p2)  # true


# In practice, you’ll find the regular expressions constructed in Python using the raw strings.

"""
Summary
  A regular expression is a string that contains the special characters for matching a string with a pattern.
  Use the Pattern object or functions in re module to search for a pattern in a string.
  Use raw strings to construct regular expression to avoid escaping the backslashes.
"""
