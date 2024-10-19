"""
7 Ways to Concatenate Strings in Python


"""

# 3) Concatenating strings using the += operator
# Similar to the + operator, you can use the += operator to concatenate multiple strings into one:
s = "String"
s += " Concatenation"
print(s)


# 4) Concatenating strings using the join() method
# The join() method allows you to concatenate a list of strings into a single string:
# In this example, we use the join() method to concatenate strings delimited by a space.
s1 = "String"
s2 = "Concatenation"

s3 = " ".join([s1, s2])
print(s3)


# The following example use the join() method to concatenate strings delimited by a comma:
s1, s2, s3 = "Python", "String", "Concatenation"
s = ",".join([s1, s2, s3])
print(s)
