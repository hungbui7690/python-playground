"""
Test if a path is a directory
- os.path.join("C:\\", "temp")
- os.path.exists()
- os.isdir()
- os.isfile()
- os.listdir()

"""

import os


# To check if a path exists and is a directory, you can use the functions os.path.exists() and os.path.isdir() functions. For example:
dir = os.path.join("C:\\", "temp")
print(dir)


path = os.getcwd()
isExist = os.path.exists(path)
print(isExist)  # True


path = "/home/User/Desktop/file.txt"
isExist = os.path.exists(path)
print(isExist)  # False


# C:\\temp must exist for this to run
if os.path.exists(dir) or os.path.isdir(dir):
    print(f"The {dir} is a directory")


print(os.listdir())  # ['# Lessons', '# pictures', '.gitignore', 'playground']
