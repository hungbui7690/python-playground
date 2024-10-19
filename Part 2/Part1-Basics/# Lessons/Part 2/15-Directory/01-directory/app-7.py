"""
Traverse a directory recursively

- The os.walk() function allows you to traverse a directory recursively. The os.walk() function returns the root directory, the sub-directories, and files.

"""

import os


# The following example shows how to print all files and directories in the c:\temp directory:

path = "c:\\temp"
for root, dirs, files in os.walk(path):
    print(f"{root} has {len(files)} files")
