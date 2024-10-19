"""
Set Comprehension


"""

# To convert the tags in the set to another set of tags in lowercase, you may use the following for loop:

tags = {"Django", "Pandas", "Numpy"}

lowercase_tags = set()
for tag in tags:
    lowercase_tags.add(tag.lower())

print(lowercase_tags)  # {'pandas', 'django', 'numpy'}


# Or you can use the built-in map() function with a lambda expression:

lowercase_tags = set(map(lambda tag: tag.lower(), tags))
print(lowercase_tags)  # {'pandas', 'django', 'numpy'}
# The map() function returns a map object so you need to use the set() function to convert it to a set.


# To make the code more concise, Python provides you with the set comprehension syntax as follows:
#   {expression for element in set if condition}

"""
    The set comprehension allows you to create a new set based on an existing set.

    A set comprehension carries the following steps:

        First, iterate over the elements of a set.
        Second, apply an expression to each element
        Third, create a new set of elements resulting from the expression.

    In addition, the set comprehension allows you to select which element to apply the expression via a condition in the if clause.

    Note that the set comprehension returns a new set, it doesn’t modify the original set.

"""

# Back to the previous example, you can convert all the tags in the tags set by using the following set comprehension:

tags = {"Django", "Pandas", "Numpy"}
lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)  # {'numpy', 'pandas', 'django'}
# This syntax definitely looks more concise than a for loop and more elegant than the map() function.
