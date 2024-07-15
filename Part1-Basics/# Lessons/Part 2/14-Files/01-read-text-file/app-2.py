"""
Read Text File

"""

import os

os.chdir(os.path.dirname(__file__))


print("////// 1 //////")
# The following example illustrates how to use the read() method to read all the contents of the the-zen-of-python.txt file into a string:
with open("zen-of-python.txt") as f:
    contents = f.read()
    print(contents)


print("////// 2 //////")


# The following example uses the readlines() method to read the text file and returns the file contents as a list of strings:
with open("zen-of-python.txt") as f:
    [print(line) for line in f.readlines()]
