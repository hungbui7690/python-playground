"""
Frozen a set


"""

# To make a set immutable, you use the built-in function called frozenset(). The frozenset() returns a new immutable set from an existing one. For example:

skills = {"Problem solving", "Software design", "Python programming"}
skills = frozenset(skills)

# After that, if you attempt to modify elements of the set, you’ll get an error:

skills.add("Django")  # AttributeError: 'frozenset' object has no attribute 'add'
