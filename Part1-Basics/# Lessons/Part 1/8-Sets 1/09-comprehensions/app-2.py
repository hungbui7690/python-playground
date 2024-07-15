"""
Set Comprehension
- Use Python set comprehension to create a new set based on an existing set by applying an expression to each element of the existing set.

"""

# Python Set comprehension with an if clause example

# Suppose you want to convert all elements of the tags set to lowercase except for the Numpy.
# To do it, you can add a condition to the set comprehension like this:

tags = {"Django", "Pandas", "Numpy"}
new_tags = {tag.lower() for tag in tags if tag != "Numpy"}

print(new_tags)  # {'pandas', 'django'}
