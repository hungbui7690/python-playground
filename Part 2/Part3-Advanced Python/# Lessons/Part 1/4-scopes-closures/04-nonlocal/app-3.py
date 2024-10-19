"""
Python nonlocal keyword

"""

# To modify variables from a nonlocal scope in a local scope, you use the nonlocal keyword. For example:


def outer():
    message = "outer scope"
    print(message)

    def inner():
        nonlocal message
        message = "inner scope"
        print(message)

    inner()

    print(message)


outer()
# outer scope
# inner scope
# inner scope


"""
In this example, we use nonlocal keyword to explicitly instruct Python that we’re modifying a nonlocal variable.

When you use the nonlocal keyword for a variable, Python will look for the variable in the enclosing local scopes chain until it first encounters the variable name.

More importantly, Python won’t look for the variable in the global scope.
"""
