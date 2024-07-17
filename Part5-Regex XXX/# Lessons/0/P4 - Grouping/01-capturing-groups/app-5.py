"""
CAPTURING GROUP

Named capturing groups

- By default, you can access a subgroup in a match using an index, for example, match.group(1). Sometimes, accessing a subgroup by a meaningful name is more convenient.
- You use the named capturing group to assign a name to a group. The following shows the syntax for assigning a name to a capturing group:

        (?P<name>rule)

- In this syntax:

    () indicates a capturing group.
    ?P<name> specifies the name of the capturing group.
    rule is a rule in the pattern.

- For example, the following creates the names:

    '(?P<resource>\w+)/(?P<id>\d+)'

- In this syntax, the resource is the name for the first capturing group and the id is the name for the second capturing group.

"""

import re


# To get all the named subgroups of a match, you use the groupdict() method of the Match object. For example:
s = "news/100"
pattern = "(?P<resource>\w+)/(?P<id>\d+)"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.groupdict())

# {'resource': 'news', 'id': '100'}


# In this example, the groupdict() method returns a dictionary where the keys are group names and values are the subgroups.
