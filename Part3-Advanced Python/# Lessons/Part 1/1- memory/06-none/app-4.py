"""
The applications of the Python None object

"""

# To fix this issue, you can use the None value as a default parameter as follows:


def append(color, colors=None):
    if colors is None:
        colors = []

    colors.append(color)
    return colors


hsl = append("hue")
print(hsl)  # ['hue']


rgb = append("red")
print(rgb)  # ['red']
