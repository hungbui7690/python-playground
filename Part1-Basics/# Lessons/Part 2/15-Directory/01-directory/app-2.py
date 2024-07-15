"""
Join and split a path

- To make a program work across platforms including Windows, Linux, and macOS, you need to use platform-independent file and directory paths.

- Python provides you with a submodule os.path that contains several useful functions and constants to join and split paths.

- The join() function joins path components together and returns a path with the corresponding path separator. For example, it uses backslash (\) on Windows and forward slash (/) on macOS or Linux.


"""

import os


# The split() function splits a path into components without a path separator. Here’s an example of using join() and split() functions:
fp = os.path.join("temp", "python")
print(fp)  # temp\python (on Windows)

pc = os.path.split(fp)
print(pc)  # ('temp', 'python')
