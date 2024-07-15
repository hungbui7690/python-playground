"""
List Files

- Sometimes, you may want to list all files from a directory for processing. For example, you might want to find all images of a directory and resize each of them. To list all files in a directory, you can use the os.walk() function.

- The os.walk() function generates file names in a directory by walking the tree either top-down or bottom-up. The os.walk() function yields a tuple with three fields (dirpath, dirnames, and filenames) for each directory in the directory tree.

** Note that the os.walk() function examines the whole directory tree. Therefore, you can use it to get all files from all directories and their subdirectories of a root directory.

"""


# 1. Suppose you have a folder D:\web with the following directories and files


# 2. The following example shows how to use the os.walk() function to list all HTML files from the D:\web directory:

import os


path = "D:\\Tools\\web"


# First, initialize a list to store the path to HTML files:
html_files = []


# Second, call os.walk() function to examine directories of the D:\web folder:
# The dirpath stores the directory and filenames store files in that directory.
for dirpath, dirnames, filenames in os.walk(path):
    # Third, loop over the filenames and add them to the html_files list if their extensions are .html:
    for filename in filenames:
        if filename.endswith(".html"):
            # Note that the os.path.join() returns the full path of the filename by joining the dirpath with the filename.
            html_files.append(os.path.join(dirpath, filename))


# Finally, print output the filenames in the html_files list:
for html_file in html_files:
    print(html_file)


"""
D:\Tools\web\about.html
D:\Tools\web\contact.html
D:\Tools\web\index.html
D:\Tools\web\blog\read-file.html
D:\Tools\web\blog\write-file.html
"""
