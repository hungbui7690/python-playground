"""
STRING JOIN

- The string join() method returns a string which is the concatenation of strings in an iterable such as a tuple, a list, a dictionary, and a set.

- The following shows the syntax of the join() method:

    str.join(iterable)

- The str will be the separator between elements in the result string.

- If the iterable contains any non-string value, the join() method will raise a TypeError. To fix it, you need to convert non-string values to strings before calling the join() method.

- The join() method has many practical applications. For example, you can use the join() method to compose a row for a CSV file.

"""


# 1) Using string join() method to concatenate multiple strings into a string
# The following example uses the string join() method to concatenate a tuple of strings without a separator:

colors = ("red", "green", "blue")
rgb = "".join(colors)
print(rgb)  # redgreenblue


# The following example uses the string join() method with the comma separator (,):

rgb = ",".join(colors)
print(rgb)  # red,green,blue
