"""
Python nonlocal

"""

# See the following example:

message = "global scope"


def outer():
    def inner():
        print(message)

    inner()


outer()  # global scope


"""
In this example, Python searches for the message variable in the local scope of the inner function.

Since Python doesn’t find the variable, it searches for the variable in its enclosing scope, which is the scope of the outer function.

And in this case, Python goes up to the global scope to find the variable: pic-2
"""
