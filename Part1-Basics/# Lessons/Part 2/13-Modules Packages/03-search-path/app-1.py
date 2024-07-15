"""
Introduction to Python module search path
- When you import a module in a program:

    import module

- Python will search for the module.py file from the following sources:

    The current folder from which the program executes.
    A list of folders specified in the PYTHONPATH environment variable, if you set it before.
    An installation-dependent list of folders that you configured when you installed Python.

"""

# Python stores the resulting search path in the sys.path variable that comes from the sys module.
# The following program shows the current module search path:

import sys

for path in sys.path:
    print(path)

# d:\Coding\BackEnd\Python\python-tutorial\Part 1 - Basics\playground
# C:\Users\7hanhHung\AppData\Local\Programs\Python\Python311\python311.zip
# C:\Users\7hanhHung\AppData\Local\Programs\Python\Python311\DLLs
# C:\Users\7hanhHung\AppData\Local\Programs\Python\Python311\Lib
# C:\Users\7hanhHung\AppData\Local\Programs\Python\Python311
# D:\Coding\BackEnd\Python\python-tutorial\Part 1 - Basics\.venv
# D:\Coding\BackEnd\Python\python-tutorial\Part 1 - Basics\.venv\Lib\site-packages


"""
    To make sure Python can always find the module.py, you need to:

        - Place module.py in the folder where the program will execute.
        - Include the folder that contains the module.py in the PYTHONPATH environment variable. Or you can place the module.py in one of the folders included in the PYTHONPATH variable.
        - Place the module.py in one of the installation-dependent folders.

"""
