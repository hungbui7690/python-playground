"""
CAPTURING GROUP

More named capturing group example

- The following pattern:

        \w+/d{4}/d{2}/d{2}

- matches this path:

        news/2021/12/31

- And you can add the named capturing groups to the pattern like this:

        '(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})'

"""

import re


# This program uses the patterns to match the path and shows all the subgroups:
s = "news/2021/12/31"
pattern = "(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.groupdict())

# {'resource': 'news', 'year': '2021', 'month': '12', 'day': '31'}


# Summary
# Place a rule of a pattern inside parentheses () to create a capturing group.
# Use the group() method of the Match object to get the subgroup by an index.
# Use the (?P<name>rule) to create a named capturing group for the rule in a pattern.
# Use the groupdict() method of the Match object to get the named subgroups as a dictionary.
