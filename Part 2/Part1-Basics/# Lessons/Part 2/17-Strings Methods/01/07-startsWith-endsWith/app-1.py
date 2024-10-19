"""
STARTSWITH

- The startswith() method returns True if a string starts with another string. Otherwise, it returns False.

- The following shows the syntax of the startswith() method:

        str.startswith(prefix, [,start [,end ])

- The startswith() method accepts three parameters:

    + prefix is a string or a tuple of strings to search for. The prefix parameter is mandatory.
    + start is the position that the method starts looking for the prefix. The start parameter is optional.
    + end is the position in the string that the method stops searching for the prefix. The end parameter is also optional.

- Note that the startswith() method is case-sensitive. In other words, it will look for the prefix case-sensitively.

"""

# 1) Using the startswith() method to check if a string begins with another string
s = "Make it work, make it right, make it fast."
result = s.startswith("Make")
print(result)  # True


# As mentioned earlier, the startswith() method searches for a string case-sensitively. Therefore, the following example returns False:
s = "Make it work, make it right, make it fast."
result = s.startswith("make")
print(result)  # False


# 2) Using the startswith() method with a tuple
s = "Make it work, make it right, make it fast."
result = s.startswith(("Make", "make"))
print(result)  # True


# 3) Using the startswith() method with the start parameter
s = "Make it work, make it right, make it fast."
result = s.startswith("make", 14)
print(result)  # True
