"""
List Slice
- Lists support the slice notation that allows you to get a sublist from a list:

      sub_list = list[begin: end: step]

- To get the n-first elements from a list, you omit the first argument:

      sub_list = list[:n]

"""


# 3) Using Python List slice to get the n-last elements from a list

# To get the n-last elements of a list, you use the negative indexes.
# For example, the following returns a list that includes the last 3 elements of the colors list:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sub_colors = colors[-3:]

print(sub_colors)  # ['blue', 'indigo', 'violet']


# 4) Using Python List slice to get every nth element from a list

# The following example uses the step to return a sublist that includes every 2nd element of the colors list:

sub_colors = colors[::2]

print(sub_colors)  # ['red', 'yellow', 'blue', 'violet']
