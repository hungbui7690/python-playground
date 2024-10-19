"""
Write Text File

"""

# The following example shows how to use the write() function to write a list of texts to a text file:
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
    for line in lines:
        f.write(line)
        f.write("\n")

# If the readme.txt file doesn’t exist, the open() function will create a new file.
