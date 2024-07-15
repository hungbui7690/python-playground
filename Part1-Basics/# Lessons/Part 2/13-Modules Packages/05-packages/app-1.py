"""
Packages
- Suppose that you need to develop a large application that handles the sales process from order to cash.
- The application will have many modules. When the number of modules grows, it’ll become difficult to keep all of them in one location.
- And you may want to group modules into something meaningful.
- This is where packages come into play.


- Packages allow you to organize modules in the hierarchical structure.
- The way Python organizes packages and modules like the Operating System structures the folders and files.
- To create a package, you create a new folder and place the relevant modules in that folder.
- To instruct Python to treat a folder containing files as a package, you need to create a __init__.py file in the folder.

*** Note that starting with Python 3.3, Python introduced the implicit namespace packages feature. This allows Python to treat a folder as a package without the __init__.py.

"""

# 1. the sales folder is the sales package
