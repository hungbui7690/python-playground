"""
Variable lookups
- In Python, scopes are nested. For example, local scopes are nested inside a module scope. And module scopes are nested inside the built-scope: pic

- When you access an object bound to a variable, Python tries to find the object:

    + in the current local scope first.
    + and goes up the chain of enclosing scopes if Python doesn’t find the object in the current scope.

"""

# The global keyword
# When you retrieve the value of a global variable from inside a function, Python automatically searches the local scope’s namespace and up the chain of all enclosing scope namespaces. For example:

counter = 10


def current():
    print(counter)


current()


# In this example, when the current() function is running, Python looks for the counter variable in the local scope.
# Since Python doesn’t find it, it searches for the variable in the global scope. And Python can find the counter variable in the global scope in this case.
# However, if you assign a value to a global variable from inside a function, Python will place that variable into the local namespace instead. For example:


def reset():
    counter = 0
    print(counter)


reset()  # 0
print(counter)  # 10


"""
At the compile time, Python interprets the counter as a local variable.

When reset() function is running, Python finds the counter in the local scope. The print(counter) statement inside the reset() function shows the value of the counter, which is zero.

When we print counter after the reset() function completes, it shows 10 instead.

In this example, the local counter variable masks the global counter variable.

If you want to access a global variable from inside a function, you can use the global keyword. For example:
"""


def resetX():
    global counter
    counter = 0
    print(counter)  # 0


resetX()  # 0

print(counter)  # 0


"""
In this example, the following statement:

  global counter

…instructs Python that the counter variable is bound to the global scope, not the local scope.

Note that it’s not a good practice to access the global variable inside a function.

\\\\\\\\\\\\\\\\\\\\

Summary

    The scopes of variables are the parts of the code where you can access the variables.
    The built-in scope is accessible from everywhere.
    The global scope (or module scope) can be accessible from every part of the module.
    The local scope is accessible from inside a function.
    Python stores the objects and their bindings in the namespace of the scope.
    Python looks up an object in the current scope first and goes up to the enclosing scope if Python doesn’t find it.
    Python scopes are nested.
    Use the global keyword if you want to access a global variable from inside a function.
"""
