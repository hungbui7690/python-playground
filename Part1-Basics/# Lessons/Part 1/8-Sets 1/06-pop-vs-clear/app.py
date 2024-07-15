"""
Returning an element from a set
- To remove and return an element from a set, you use the pop() method.

- Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.

"""

# If you execute the following code multiple times, it’ll show a different value each time:

skills = {"Problem solving", "Software design", "Python programming"}
skill = skills.pop()

print(skill)  # Software design


# Removing all elements from a set
# To remove all elements from a set, you use the clear() method:

skills = {"Problem solving", "Software design", "Python programming"}
skills.clear()

print(skills)  # set()
