"""
Python Context Managers


"""

# To fix this, you may use the try...except...finally statement:

try:
    f = open(".\\playground\\data.txt")
    data = f.readlines()
    # convert the number to integer and display it
    print(int(data[0]))
except ValueError as error:
    print(error)
finally:
    f.close()

# invalid literal for int() with base 10: '"100"'


"""
Since the code in the finally block always executes, the code will always close the file properly.

This solution works as expected. However, it’s quite verbose.

Therefore, Python provides you with a better way that allows you to automatically close the file after you complete processing it.

This is where context managers come into play.
"""
