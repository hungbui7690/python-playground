"""
Python with statement
- Here is the typical syntax of the with statement:

        with context as ctx:
            # use the the object
        # context is cleaned up

- How it works.

    + When Python encounters the with statement, it creates a new context. The context can optionally return an object.
    + After the with block, Python cleans up the context automatically.
    The scope of the ctx has the same scope as the with statement. It means that you can access the ctx both inside and after the with statement.

"""

# The following shows how to access the f variable after the with statement:

with open(".\\playground\\data.txt") as f:
    data = f.readlines()
    print(int(data[0]))


print(f.closed)  # True

# ValueError: invalid literal for int() with base 10: '"100"'
