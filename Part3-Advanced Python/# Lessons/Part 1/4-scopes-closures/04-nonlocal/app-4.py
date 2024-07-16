"""
Python nonlocal keyword

"""

# Consider the following example:

message = "outer scope"


def outer():
    print(message)

    def inner():
        nonlocal message
        message = "inner scope"
        print(message)

    inner()

    print(message)


outer()
# If you run this code, you’ll get the following error:
# SyntaxError: no binding for nonlocal 'message' found


"""
From inside of the inner function, we use the nonlocal keyword for the message variable.

Therefore, Python searches for the message variable in the enclosing scope, which is the scope of the outer function.

Since the scope of the outer function doesn’t have message variable and Python doesn’t look further in the global scope, it issues an error: pic-3

\\\\\\\\\\\\\\\\\\\\\\

Summary

  The enclosing scopes of inner functions are called nonlocal scopes.
  Use the nonlocal keyword to modify the variable from the nonlocal scopes.
  And Python will look up the nonlocal variables in the enclosing local scopes chain. It won’t search for the variable in the global scope.

"""
