"""
Rename File

- To rename a file, you use the os.rename() function:

    os.rename(src,dst)

- If the src file does not exist, the os.rename() function raises a FileNotFound error. Similarly, if the dst already exists, the os.rename() function issues a FileExistsError error.

"""

import os


# 1) For example, the following uses the os.rename() function to rename the file readme.txt to notes.txt:
# os.rename(".\\playground\\readme.txt", ".\\playground\\notes.txt")


# 2) To avoid an error if the readme.txt doesn’t exist and/or the notes.txt file already exists, you can use the try...except statement:
try:
    os.rename(".\\playground\\readme.txt", ".\\playground\\notes.txt")
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
