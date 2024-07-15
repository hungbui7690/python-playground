"""
Delete a directory

"""

import os


# To delete a directory, you use the os.rmdir() function as follows:

dir = os.path.join("C:\\", "temp", "python3")

if os.path.exists(dir):
    os.rmdir(dir)
    print(dir + " is removed.")
