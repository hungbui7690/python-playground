"""
Python Data vs. Non-data Descriptors
- Descriptors have two types:

    Data descriptors are objects of a class that implements __set__ method (and/or __delete__ method)
    Non-data descriptors are objects of a class that have the __get__ method only.

- Both descriptor types can optionally implement the __set_name__ method. The __set_name__ method doesn’t affect the classification of the descriptors.

- The descriptor types determine how Python resolves object’s attributes lookup.



Non-data descriptor

- If a class uses a non-data descriptor, Python will search the attribute in instance attributes first (instance.__dict__). If Python doesn’t find the attribute in the instance attributes, it’ll use the data descriptor.

"""

import os


# First, define a non-data descriptor class FileCount that has the __get__ method which returns the number of files in a folder:
class FileCount:
    def __get__(self, instance, owner):
        print("The __get__ was called")
        return len(os.listdir(instance.path))


# Second, define a Folder class that uses the FileCount descriptor:
class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path


# Third, create an instance of the Folder class and access the count attribute:
folder = Folder("/")
print("file count: ", folder.count)


# Python called the __get__ descriptor:
# The __get__ was called
# file count:  7


# After that, set the count attribute of the folder instance to 100 and access the count attribute:
folder.__dict__["count"] = 100
print("file count: ", folder.count)  # file count:  100

# In this example, Python can find the count attribute in the instance dictionary __dict__. Therefore, it does not use data descriptors.
