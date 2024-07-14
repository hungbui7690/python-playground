"""
Introduction to the Python Set type

- A Python set is an unordered list of immutable elements. It means:

    + Elements in a set are unordered.
    + Elements in a set are unique. A set doesn’t allow duplicate elements.
    + Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.

"""

# To define a set in Python, you use the curly brace {}. For example:

skills = {"Python programming", "Databases", "Software design"}

# Note a dictionary also uses curly braces, but its elements are key-value pairs.
# To define an empty set, you cannot use the curly braces like this:
# …because it defines an empty dictionary.

empty_set = {}


# Therefore, you need to use the built-in set() function:

empty_set = set()


# An empty set evaluates to False in Boolean context. For example:

skills = set()
print(bool(skills))  # False

if not skills:
    print("Empty sets are falsy")


# In fact, you can pass an iterable to the set() function to create a set. For example, you can pass a list, which is an iterable, to the set() function like this:

skills = set(["Problem solving", "Critical Thinking"])
print(skills)  # {'Problem solving', 'Critical Thinking'}
# Note that the original order of elements may not be preserved.


# If an iterable has duplicate elements, the set() function will remove them. For example:

characters = set("letter")
print(characters)  # {'t', 'r', 'e', 'l'}
# In this example, the string 'letter' has two e and t characters and the set() removes each of them.
