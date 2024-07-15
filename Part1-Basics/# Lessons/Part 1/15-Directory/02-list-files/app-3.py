"""
Make list files function more efficient

- If the number of files is small, the list_files() function works fine. However, when the number of files is large, returning a large list of files is not memory efficient.

"""


# 1. Suppose you have a folder D:\web with the following directories and files

# To resolve this, you can use a generator to yield each file at a time instead of returning a list:
import os


def list_files(path, extentions=None):
    """List all files in a directory specified by path"""

    for root, _, files in os.walk(path):
        for file in files:
            if extentions is None:
                yield os.path.join(root, file)
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        yield os.path.join(root, file)


if __name__ == "__main__":
    filepaths = list_files(r"D:\web", (".html", ".css"))
    for filepath in filepaths:
        print(filepath)
