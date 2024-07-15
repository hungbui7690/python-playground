"""
Delete File

"""

# 1) To delete a file, you use the remove() function of the os built-in module. For example, the following uses the os.remove() function to delete the readme.txt file:
import os

os.remove(".\\playground\\readme.txt")
# If the readme.txt file doesn’t exist, the os.remove() function will issue an error:
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'readme.txt'


# 2) To avoid the error, you can check the file exists before deleting it like this:
filename = ".\\playground\\readme.txt"
if os.path.exists(filename):
    os.remove(filename)


# 3) Alternatively, you can use the try...except statement to catch the exception if the file doesn’t exist:
try:
    os.remove(".\\playground\\readme.txt")
except FileNotFoundError as e:
    print(e)
