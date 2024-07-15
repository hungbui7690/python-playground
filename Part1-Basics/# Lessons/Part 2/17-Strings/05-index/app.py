"""
String index()

- The string index() method returns the lowest index of a substring in a string.

- The following shows the syntax of the index() method:

        str.index(sub[, start[, end]])

- The index() method has three parameters:

    sub is the substring to search for in the str.
    start and end parameters are interpreted as in the slice notation str[start:end]. The slice specifies where to look for the substring sub. Both start and end parameters are optional.

- If the str doesn’t contain the substring sub within the slice str[start:end], the index() method will raise a ValueError.

- If you don’t want to receive the ValueError when the sub is not found, you can use the string find() method instead. The find() method returns -1 instead of raising the ValueError.

*** Note that if you just want to check if a substring is in a string, you can use the in operator.

"""

# 1) Using the Python string index() method to find the position of a substring in a string
# The following example shows how to use the index() method to find the substring 'Python' in the string 'Python will, Python will rock you.':

s = "Python will, Python will rock you."
position = s.index("Python")
print(position)  # 0

# Since the string has two substrings 'Python', the index() method returns the lowest index where the substring found in the string.


# 2) Using the Python string index() method to find the position of a substring in a string within a slice
# The following example uses the index() method to find the substring 'Python' in the string 'Python will, Python will rock you.' within the slice str[1:]:

s = "Python will, Python will rock you."
position = s.index("Python", 1)
print(position)  # 13

# In this example, the index() method returns the position of the second occurrence of the substring in the string.


# 3) The substring doesn’t exist in the string example
# The following example raises a ValueError because the substring 'Java' doesn’t exist in the string 'Python will, Python will rock you.':

s = "Python will, Python will rock you."
position = s.index("Java")
print(position)  # ValueError: substring not found


# Summary

# Use the index() to get the lowest index of a substring within a string.
# The index() method raises a ValueError if the string doesn’t contain the substring.
