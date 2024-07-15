"""
Directory

- Get the current working directory

        os.getcwd()

- Change the current working directory

        os.chdir(".\\playground")


"""

# The current working directory is the directory where the Python script is running. To get the current working directory, you use the os.getcwd() as follows:
import os

cwd = os.getcwd()
print(cwd)  # D:\Coding\BackEnd\Python\python-tutorial\Part 1 - Basics


# To change the current working directory, you use the function os.chdir():
os.chdir(".\\playground")
cwd = os.getcwd()
print(cwd)
