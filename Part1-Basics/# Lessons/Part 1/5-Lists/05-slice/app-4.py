"""
List Slice

"""


# 5) Using Python List slice to reverse a list

# When you use a negative step, the slice includes the list of elements starting from the last element to the first element. In other words, it reverses the list. See the following example:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
reversed_colors = colors[::-1]

print(reversed_colors)
# ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']


# 6) Using Python List slice to substitute part of a list

# Besides extracting a part of a list, the list slice allows you to change the list element.
# The following example changes the first two elements in the colors list to the new values:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colors[0:2] = ["black", "white"]

print(colors)
# ['black', 'white', 'yellow', 'green', 'blue', 'indigo', 'violet']


# 7) Using Python List slice to partially replace and resize a list

# The following example uses the list slice to replace the first and second elements with the new ones and also add a new element to the list:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(f"The list has {len(colors)} elements")

colors[0:2] = ["black", "white", "gray"]
print(colors)
print(f"The list now has {len(colors)} elements")
# ['black', 'white', 'gray', 'yellow', 'green', 'blue', 'indigo', 'violet']


# 8) Using Python list slice to delete elements

# The following shows how to use the list slice to delete the 3rd, 4th, and 5th elements from the colors list:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
del colors[2:5]

print(colors)  # ['red', 'orange', 'indigo', 'violet']
