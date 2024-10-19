"""
Python Generators
- Typically, Python executes a regular function from top to bottom based on the run-to-completion model.
- It means that Python cannot pause a regular function midway and then resumes the function after that.

"""


def greeting():
    print("Hi!")
    print("How are you?")
    print("Are you there?")


# When Python executes the greeting() function, it executes the code line by line from top to bottom.
# Also, Python cannot pause the function at the last line.
# … and jumps to another code and resumes the execution from that line.
# To pause a function midway and resume from where the function was paused, you use the yield statement.


# When a function contains at least one yield statement, it’s a generator function.
# By definition, a generator is a function that contains at least one yield statement.


# When you call a generator function, it returns a new generator object. However, it doesn’t start the function.
# Generator objects (or generators) implement the iterator protocol. In fact, generators are lazy iterators. Therefore, to execute a generator function, you call the next() built-in function on it.
