"""
7 Ways to Concatenate Strings in Python


"""

# 5) Concatenating strings using the %-formatting
# String objects have the built-in % operator that allows you to format strings. Also, you can use it to concatenate strings. For example:

s1, s2, s3 = "Python", "String", "Concatenation"
s = "%s %s %s" % (s1, s2, s3)
print(s)  # Python String Concatenation
# In this example, Python substitutes a %s in the literal string by corresponding string variable in the tuple that follows the % operator.


# 6) Concatenating strings using the format() method
# You can use the format() method to concatenate multiple strings into a string. For example:
s1, s2, s3 = "Python", "String", "Concatenation"
s = "{} {} {}".format(s1, s2, s3)
print(s)
# In this example, you use the {} in the string literal and pass the string that you want to concatenate to the format() method. The format() method substitutes the {} by the corresponding string argument.


# 7) Concatenating strings using f-strings
# Python 3.6 introduced the f-strings that allow you to format strings in a more concise and elegant way.
# And you can use the f-strings to concatenate multiple strings into one. For example:

s1, s2, s3 = "Python", "String", "Concatenation"
s = f"{s1} {s2} {s3}"
print(s)


# Which method should you use to concatenate strings
#
# Even though there’re multiple ways to concatenate strings in Python, it’s recommended to use the join() method, the + operator, and f-strings to concatenate strings.
