"""
Write Text File

"""

# The following shows how to write a list of text strings to a text file:
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
    f.writelines(lines)
