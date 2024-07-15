"""
Write Text File

"""

# If you treat each element of the list as a line, you need to concatenate it with the newline character like this:
lines = [
    "Readme",
    " ",
    "How to write text files in Python",
    " ",
    "- First, call open()",
    "- Second, write file",
    "- Third, close file",
]
with open(".\\playground\\readme.txt", "w") as f:
    f.write("\n".join(lines))
