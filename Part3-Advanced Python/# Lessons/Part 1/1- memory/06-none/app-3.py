"""
The applications of the Python None object

"""

# 2) Using the Python None object to fix the mutable default argument issue
# The following function appends a color to a list:


def append(color, colors=[]):
    colors.append(color)
    return colors


# It works as expected if you pass an existing list:
colors = ["red", "green"]
append("blue", colors)

print(colors)  # ['red', 'green', 'blue']


# However, the problem arises when you use the default value of the second parameter. For example:
hsl = append("hue")
print(hsl)  # ['hue']

rgb = append("red")
print(rgb)  # ['hue', 'red']

# The issue is that the function creates the list once defined and uses the same list in each successive call.
