"""
Python Context Managers
- A context manager is an object that defines a runtime context executing within the with statement.
- Let’s start with a simple example to understand the context manager concept.
- Suppose that you have a file called data.txt that contains an integer 100.

"""

# The following program reads the data.txt file, converts its contents to a number, and shows the result to the standard output:

f = open(".\\playground\\data.txt")
data = f.readlines()

# convert the number to integer and display it
print(int(data[0]))  ## 100

f.close()


"""
The code is simple and straightforward.

However, the data.txt may contain data that cannot be converted to a number. In this case, the code will result in an exception.

For example, if the data.txt contains the string '100' instead of the number 100, you’ll get the following error:

    ValueError: invalid literal for int() with base 10: "'100'"

Because of this exception, Python may not close the file properly.

"""
