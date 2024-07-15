"""
Defining a reusable list files function

- List all files in a directory specified by path

    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions

"""


# 1. Suppose you have a folder D:\web with the following directories and files

# 2. By using the os.walk() function, we can define a reusable list_files() function like this:
import os


def list_files(path, extentions=None):
    """List all files in a directory specified by path"""
    filepaths = []
    for root, _, files in os.walk(path):
        for file in files:
            if extentions is None:
                filepaths.append(os.path.join(root, file))
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        filepaths.append(os.path.join(root, file))

    return filepaths


if __name__ == "__main__":
    filepaths = list_files(r"D:\Tools\web", (".html", ".css"))
    for filepath in filepaths:
        print(filepath)


"""
D:\Tools\web\about.html
D:\Tools\web\contact.html
D:\Tools\web\index.html
D:\Tools\web\assets\css\style.css
D:\Tools\web\blog\read-file.html
D:\Tools\web\blog\write-file.html
"""
