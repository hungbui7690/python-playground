"""
ENDSWITH

- The endswith() is a string method that returns True if a string ends with another string. Otherwise, it returns False.

- The following illustrates the syntax of the endswith() method:

    str.endswith(suffix, [,start [,end ])


- The endswith() method has three parameters:

    + suffix is a string or a tuple of strings to match in the str. If the suffix is a tuple, the method will return True if the str ends with one of the string element in the tuple. The suffix parameter is mandatory.
    + start is the position that the method starts searching for the suffix. The start parameter is optional.
    + end is the position in the str that the method stops searching for the suffix. The end parameter is also optional.

- The endswith() method searches for the suffix case-sensitively.

- To determine if a string starts with another string, you use the string startswith() method.

"""

# 1) Using the Python string endswith() method to determine if a string ends with another string
s = "Beautiful is better than ugly"
result = s.endswith("ugly")
print(result)  # True


# As mentioned above, the endswith() method matches the string case-sensitively. So the following example returns False:
s = "Beautiful is better than ugly"
result = s.endswith("UGLY")
print(result)  # False


# 2) Using the Python string endswith() method with a tuple
# The following example uses the endswith() method to check if a sentence ends with a fullstop (.), a question mark (?), or an exclamation mark (!):
marks = (".", "?", "!")
sentence = "Hello, how are you?"
result = sentence.endswith(marks)
print(result)  # True
