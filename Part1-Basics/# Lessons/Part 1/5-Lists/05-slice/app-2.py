"""
List Slice
- Lists support the slice notation that allows you to get a sublist from a list:

      sub_list = list[begin: end: step]

- To get the n-first elements from a list, you omit the first argument:

      sub_list = list[:n]

"""


# 2) Using Python List slice to get the n-first elements from a list


# The following example returns a list that includes the first three elements from the colors list:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sub_colors = colors[:3]

print(sub_colors)  # ['red', 'orange', 'yellow']
# Notice that the colors[:3] is equivalent to the color[0:3].
