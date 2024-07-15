"""
Read Text File

"""

print("////// 3 //////")


# The reason you see a blank line after each line from a file is that each line in the text file has a newline character (\n). To remove the blank line, you can use the strip() method. For example:
with open(".\\playground\\zen-of-python.txt") as f:
    [print(line.strip()) for line in f.readlines()]


print("////// 4 //////")


# The following example shows how to use the readline() to read the text file line by line:
with open(".\\playground\\zen-of-python.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
