"""
Read Text File

"""

print("////// 5 //////")


# A more concise way to read a text file line by line
# The open() function returns a file object which is an iterable object. Therefore, you can use a for loop to iterate over the lines of a text file as follows:
with open(".\\playground\\zen-of-python.txt") as f:
    for line in f:
        print(line.strip())

# This is a more concise way to read a text file line by line.
