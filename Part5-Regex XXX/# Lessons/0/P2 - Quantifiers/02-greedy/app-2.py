"""
How Python regex greedy mode works

- First, the regex engine starts matching from the first character in the string s.

- Next, because the first character is < which does not match the quote ("), the regex engine continues to match the next characters until it reaches the first quote ("): pic-1

- Then, the regex engine examines the pattern and matches the string with the next rule .+.

- Because the .+ rule matches a character one or more times, the regex engine matches all characters until it reaches the end of the string: pic-2

- After that, the regex engine examines the last rule in the pattern, which is a quote (“). However, it already reaches the end of the string. There’s no more character to match. It is too greedy to go too far.

- Finally, the regex engine goes back from the end of the string to find the quote (“). This step is called backtracking. pic-3

- As a result, the match is the following substring which is not what we expected: pic-4

        "submit" class="btn"

- To fix this issue, you need to instruct the quantifier (+) to use the non-greedy (or lazy) mode instead of the greedy mode.

- To do that, you add a question mark (?) after the quantifier like this:

        ".+?"

"""

import re

s = '<button type="submit" class="btn">Send</button>'

pattern = '".+?"'
matches = re.finditer(pattern, s)

for match in matches:
    print(match.group())

# "submit"
# "btn"


# Summary
# By default, all quantifiers use the greedy mode.
# Greedy quantifiers will match their preceding elements as much as possible.
