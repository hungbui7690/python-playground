"""
Raw Strings

"""

# 1. Use raw strings to handle file path on Windows
# Windows OS uses backslashes to separate paths. For example:
# c:\user\tasks\new


# 2. If you use this path as a regular string, Python will issue a number of errors:
# dir_path = 'c:\user\tasks\new'
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# Python treats \u in the path as a Unicode escape but couldn’t decode it.

# 3. Now, if you escape the first backslash, you’ll have other issues:
dir_path = "c:\\user\tasks\new"
print(dir_path)
# c:\user asks
# ew


# 4. In this example, the \t is a tab and \n is the new line.
# To make it easy, you can turn the path into a raw string like this:
dir_path = r"c:\user\tasks\new"
print(dir_path)  # c:\user\tasks\new
