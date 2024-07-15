"""
Check If File Exists
- When processing files, you’ll often want to check if a file exists before doing something else with it such as reading from the file or writing to it.
- To do it, you can use the exists() function from the os.path module or is_file() method from the Path class in the pathlib module.

    + os.path.exists() function

        from os.path import exists
        file_exists = exists(path_to_file)


    + Path.is_file() method

        from pathlib import Path
        path = Path(path_to_file)
        path.is_file()


    1) Using os.path.exists() function to check if a file exists
        - To check if a file exists, you pass the file path to the exists() function from the os.path standard library.

"""

# First, import the os.path standard library:
import os


# Second, call the exists() function:
file_exists = os.path.exists(".\\playground\\readme.txt")

print(file_exists)

"""
    If the file exists, the exists() function returns True. Otherwise, it returns False.

    If the file is in the same folder as the program, the path_to_file is just simply the file name.

    However, it’s not the case, you need to pass the full file path of the file. For example: /path/to/filename
"""
