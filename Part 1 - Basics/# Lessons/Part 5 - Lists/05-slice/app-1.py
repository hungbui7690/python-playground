"""
List Slice
- Lists support the slice notation that allows you to get a sublist from a list:

      sub_list = list[begin: end: step]

- In this syntax, the begin, end, and step arguments must be valid indexes. And they’re all optional.

- The begin index defaults to zero. The end index defaults to the length of the list. And the step index defaults to 1.

- The slice will start from the begin up to the end in the step of step.

- The begin, end, and step can be positive or negative. Positive values slice the list from the first element to the last element while negative values slice the list from the last element to the first element.

- In addition to extracting a sublist, you can use the list slice to change the list such as updating, resizing, and deleting a part of the list.

"""


# 1) Basic Python list slice example
# Suppose that you have the following list of strings:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# The following example uses the list slice to get a sublist from the colors list:

sub_colors = colors[1:4]
print(sub_colors)  # ['orange', 'yellow', 'green']

"""
  The begin index is 1, so the slice starts from the 'orange' color. The end index is 4, therefore, the last element of the slice is 'green'.

  As a result, the slice creates a new list with three colors: ['orange', 'yellow', 'green'].

  This example doesn’t use the step, so the slice gets all values within the range without skipping any elements.
"""
