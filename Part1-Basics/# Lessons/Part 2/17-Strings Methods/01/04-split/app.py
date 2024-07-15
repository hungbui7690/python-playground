"""
STRING SPLIT

- The split() method splits a string and returns a list of substrings. The following shows the syntax of the split() method:

        str.split(sep=None, maxsplit=-1)

-  The split() method accepts two optional parameters:

    1) sep parameter

    - The sep parameter is the delimiter that specifies where in the str each split should occurs.

    - If you don’t pass the sep argument or use None, the split() method will treat consecutive whitespace as a single delimiter and return a list of non-empty substrings.


    2) maxsplit parameter

    - The maxsplit parameter specifies the maximum number of splits that the method will carry.

    - If you pass the maxsplit, the result list will have at most maxsplit + 1 elements.

    - If you omit the maxsplit or pass -1, then there’s no limit on the number of splits. In other words, the result list will contain all possible splits.

"""

# 1) Using the Python String split() method to split a string into words
# The following example illustrates how to sue the split() method to split a string into multiple words:

s = "Python String split"
substrings = s.split()
print(substrings)  # ['Python', 'String', 'split']
# In this example, we didn’t pass any argument to the split() method. Therefore, the split() method splits the strings into words with all possible splits.


# 2) Using the Python String split() method to split a string using a separator
# The following example shows how to use the split() method to split a string using the comma (,) separator:

s = "John,Doe,john.doe@example.com,(408)-999-1111"
contact = s.split(",")
print(contact)  # ['John', 'Doe', 'john.doe@example.com', '(408)-999-1111']


# 3) Using the Python String split() method to split a string using the sep and maxsplit parameters
# The following example illustrates how to use the split() method with the maxsplit parameter:

s = "apple,orange,banana"
results = s.split(",", 1)
print(results)  # ['apple', 'orange,banana']
# Since the maxsplit is one, the number of elements in the results list is two.


# If you pass -1 or skip passing the maxsplit argument, the split() will return all possible splits:
s = "apple,orange,banana"
results = s.split(",", -1)
print(results)  # ['apple', 'orange', 'banana']
