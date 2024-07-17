"""
A simple Python generator example


"""


def greeting():
    print("Hi!")
    yield 1
    print("How are you?")
    yield 2
    print("Are you there?")
    yield 3


"""
Since the greeting() function contains the yield statements, it’s a generator function.

The yield statement is like a return statement in a function. However, there’s a big difference.

When Python encounters the yield statement, it returns the value specified in the yield. In addition, it pauses the execution of the function.

If you “call” the same function again, Python will resume from where the previous yield statement was encountered.
"""


# When you call a generator function, it returns a generator object. For example:
messenger = greeting()


# The messenger is a generator object, which is also an iterator.
# To actually execute the body of the greeting() function, you need to use the next() built-in function:
result = next(messenger)
print(result)
# Hi!
# 1


# Also, it’s paused right at the first yield statement. If you “call” the greeting() function again, it’ll resume the execution from the last yield statement:
result = next(messenger)
print(result)
# How are you?
# 2


# And you can call it again:
result = next(messenger)
print(result)
# Are you there?
# 3


# However, if you execute the generator once more time, it’ll raise the StopIteration exception because it’s an iterator:
# next(messenger) # StopIteration
