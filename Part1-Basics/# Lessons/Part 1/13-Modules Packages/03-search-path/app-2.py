"""
Modifying the Python module search path at runtime
- Python allows you to modify the module search path at runtime by modifying the sys.path variable. This allows you to store module files in any folder of your choice.


"""

# 1. Create D:\Tools\python\greeting.py

# 2. The following example adds the D:\Tools\python to the search path and use the "greeting.py" module stored in this folder:

import sys


# Since the sys.path is a list, you can append a search-path to it.
# Method 1
sys.path.append("D:\\Tools\\python")
# Method 2
sys.path.insert(0, "D:\\Tools\\python")
sys.path.insert(0, ["D:\\", "D:\\Tools", "D:\\Tools\\python"])


# Print all the paths
print(sys.path)


# Can import and use
import greeting

greeting.say_hi()


"""
  Summary

      When you import a module, Python will search for the module file from the folders specified in the sys.path variable.
      Python allows you to modify the module search path by changing, adding, and removing elements from the sys.path variable.

"""
