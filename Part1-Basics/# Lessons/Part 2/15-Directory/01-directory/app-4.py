"""
Create a directory

- To create a new directory, you use os.mkdir() function. And you should always check if a directory exists first before creating a new directory.

    os.mkdir()

"""

import os


# The following example creates a new directory called python under the c:\temp directory.
# Folder C:\temp must exist, otherwise, error
dir = os.path.join("C:\\", "temp", "python")
if not os.path.exists(dir):
    os.mkdir(dir)
