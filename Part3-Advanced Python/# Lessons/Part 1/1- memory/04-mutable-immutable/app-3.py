"""
Mutable and Immutable
- It’s important to understand that immutable objects are not something frozen or absolutely constant. Let’s take a look at an example.

"""

# The following defines a tuple whose elements are the two lists:
low = [1, 2, 3]
high = [4, 5]

rankings = (low, high)


# Since the rankings is a tuple, it’s immutable. So you cannot add a new element to it or remove an element from it. pic-5


# However, the rankings tuple contains two lists that are mutable objects. Therefore, you can add a new element to the high list without any issue:
high.append(6)
print(rankings)  # ([1, 2, 3], [4, 5, 6])


# Summary
# An object whose internal state cannot be changed is called immutable for example a number, a string, and a tuple.
# An object whose internal state can be changed is called mutable for example a list, a set, and a dictionary.
