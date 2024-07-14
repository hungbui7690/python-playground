"""
Unpack a List

"""


# The following example defines a list of strings:

colors = ["red", "blue", "green"]

# To assign the first, second, and third elements of the list to variables, you may assign individual elements to variables like this:
red = colors[0]
blue = colors[1]
green = colors[2]


# However, Python provides a better way to do this. It’s called sequence unpacking.
# Basically, you can assign elements of a list (and also a tuple) to multiple variables. For example:
red, blue, green = colors
print(red, green, blue)  # red green blue


# This statement assigns the first, second, and third elements of the colors list to the red, blue, and green variables.
# In this example, the number of variables on the left side is the same as the number of elements in the list on the right side.
# If you use a fewer number of variables on the left side, you’ll get an error. For example:

colors = ["red", "blue", "green"]
red, blue = colors  # error: ValueError: too many values to unpack (expected 2)
# In this case, Python could not unpack three elements to two variables.
