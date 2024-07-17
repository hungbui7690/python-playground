"""
Python Context Managers


"""

# The following shows how to use a context manager to process the data.txt file:

with open(".\\playground\\data.txt") as f:
    data = f.readlines()
    print(int(data[0]))

# ValueError: invalid literal for int() with base 10: '"100"'
# In this example, we use the open() function with the with statement. After the with block, Python will close automatically.
