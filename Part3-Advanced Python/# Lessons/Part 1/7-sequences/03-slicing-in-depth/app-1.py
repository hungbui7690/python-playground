"""
Slicing in Depth



"""

# Python slicing review
# So far you’ve learned about slicing such as list slicing.
# Technically, slicing relies on indexing. Therefore, slicing only works with sequence types.
# For mutable sequence types such as lists, you can use slicing to extract and assign data. For example:

colors = ["red", "green", "blue", "orange"]

# extract data
print(colors[1:3])  # ['green', 'blue']

# assign data
colors[1:3] = ["pink", "black"]
print(colors)  # ['red', 'pink', 'black', 'orange']


# However, you can use slicing to extract data from immutable sequences. For example:
topic = "Python Slicing"

# Extract data
print(topic[0:6])  # Python

# If you attempt to use slicing to assign data to an immutable sequence, you’ll get an error. For example:
# topic[0:6] = "Java" # TypeError: 'str' object does not support item assignment
