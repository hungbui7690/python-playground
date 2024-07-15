"""
Check If File Exists


"""

# To make the call to the exists() function shorter and more obvious, you can import that function and rename it to file_exists() function like this:
from os.path import exists as file_exists


is_exists = file_exists(".\\playground\\readme.txt")
print(is_exists)
