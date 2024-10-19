"""
Rename a directory

    os.rename(oldPath, newPath)


"""


# To rename the directory, you use the os.rename() function:

import os

oldPath = os.path.join("C:\\", "temp", "python")
newPath = os.path.join("C:\\", "temp", "python3")

if os.path.exists(oldPath) and not os.path.exists(newPath):
    os.rename(oldPath, newPath)
    print("'{0}' was renamed to '{1}'".format(oldPath, newPath))
