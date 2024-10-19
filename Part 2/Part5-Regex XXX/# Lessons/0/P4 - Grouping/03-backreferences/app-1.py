"""
BACKREFERENCES

- Backreferences like variables in Python. The backreferences allow you to reference capturing groups within a regular expression.

- The following shows the syntax of a backreference:

        \ N

- Alternatively, you can use the following syntax:

        \g<N>

- In this syntax, N can be 1, 2, 3, etc. that represents the corresponding capturing group.

- Note that the \g<0> refer to the entire match, which has the same value as the match.group(0).

- Suppose you have a string with the duplicate word Python like this:

        s = 'Python Python is awesome'

- And you want to remove the duplicate word (Python) so that the result string will be:

        Python is awesome

- To do that, you can use a regular expression with a backreference.

    + First, match a word with one or more characters and one or more space:

            '\w+\s+'

    + Second, create a capturing group that contains only the word characters:

            '(\w+)\s+'

    + Third, create a backreference that references the first capturing group:

            '(\w+)\s+\1'

    + In this pattern, the \1 is a backreference that references the (\w+) capturing group.

"""

import re


# Finally, replace the entire match with the first capturing group using the sub() function from the re module:
s = "Python Python is awesome"

new_s = re.sub(r"(\w+)\s+\1", r"\1", s)

print(new_s)

# Python is awesome
