"""
Checking if an element is in a set

- To check if a set contains an element, you use the in operator:

        element in set

"""


# The in operator returns True if the set contains the element. Otherwise, it returns False. For example:

ratings = {1, 2, 3, 4, 5}
rating = 1

if rating in ratings:
    print(f"The set contains {rating}")


# To negate the in operator, you use the not operator. For example:

rating = 6

if rating not in ratings:
    print(f"The set does not contain {rating}")
