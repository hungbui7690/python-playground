"""
Introduction to the Python *args parameter

- When a function has a parameter preceded by an asterisk (*), it can accept a variable number of arguments. And you can pass zero, one, or more arguments to the *args parameter.

- In Python, the parameters like *args are called variadic parameters. Functions that have variadic parameters are called variadic functions.

- Note that you don’t need to name args for a variadic parameter. For example, you can use any meaningful names like *numbers, *strings, *lists, etc.

- However, by convention, Python uses the *args for a variadic parameter.


"""

# 1) Let’s take a look at the following example:


def add(*args):
    print(args)


add()  # ()
# The add function shows an empty tuple.


# 2) The following shows the type of the args argument and its contents:


def addX(*args):
    print(type(args))
    print(args)


addX()  # <class 'tuple'> + ()
# Since we didn’t pass any argument to the add() function, the output shows an empty tuple.


# 3) The following passes three arguments to the add() function:


def add(*args):
    print(args)


add(1, 2, 3)  # (1, 2, 3)


# 4) Now, the args has three numbers 1, 2, and 3. To access each element of the args argument, you use the square bracket notation [] with an index:


def add(*args):
    print(args[0])
    print(args[1])
    print(args[2])


add(1, 2, 3)


# 5) Also, you an use a for loop to iterate over the elements of the tuple.
# The following shows how to add all numbers of the args tuple in the add() function:


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


total = add(1, 2, 3)
print(total)  # 6
