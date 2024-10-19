"""
Index Error

"""

# When an exception occurs, Python stops the program unless you handle it. To handle an exception, you use the try...except statement. For example:

colors = ["red", "green", "blue"]

try:
    print(colors[3])
except IndexError as e:
    print(e)


print("Continue to run")
# <class 'IndexError'> - list index out of range
# Continue to run


# In this example, we use the try...except statement to handle the IndexError exception. As you can see from the output, the program continues to run after the try...except statement.
# The IndexError class inherits from the LookupError class which inherits from the Exception class: pic-2
