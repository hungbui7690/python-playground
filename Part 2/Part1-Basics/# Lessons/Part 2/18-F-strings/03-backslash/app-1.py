"""
Introduction to the Python backslash

- In Python, the backslash(\) is a special character. If you use the backslash in front of another character, it changes the meaning of that character.

- For example, the t is a literal character. But if you use the backslash character in front of the letter t, it’ll become the tab character (\t).

- Generally, the backslash has two main purposes.

- First, the backslash character is a part of special character sequences such as the tab character \t or the new line character \n.

"""

# The following example prints a string that has a newline character:
print("Hello,\n World")
# Hello,
#  World


# The \n is a single character, not two. For example:
s = "\n"
print(len(s))  # 1


# Second, the backslash (\) escape other special characters. For example, if you have a string that has a single quote inside a single-quoted string like the following string, you need to use the backslash to escape the single quote character:
s = '"Python\'s awesome" She said'
print(s)  # "Python's awesome" She said
