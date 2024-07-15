"""
Check If File Exists

    2) Using the pathlib module to check if a file exists
        - Python introduced the pathlib module since the version 3.4.

        - The pathlib module allows you to manipulate files and folders using the object-oriented approach.

        - If you’re not familiar with object-oriented programming, check out the Python OOP section.

"""

# First, import the Path class from the pathlib module:
from pathlib import Path


# Then, instantiate a new instance of the Path class and initialize it with the file path that you want to check for existence:
path_to_file = ".\\playground\\readme.txt"
path = Path(path_to_file)

# Finally, check if the file exists using the is_file() method:
if path.is_file():
    print(f"The file {path_to_file} exists")
else:
    print(f"The file {path_to_file} does not exist")
