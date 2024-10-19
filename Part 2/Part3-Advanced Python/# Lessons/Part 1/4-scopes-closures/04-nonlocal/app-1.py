"""
Python nonlocal

"""

# In Python, you can define a function inside another function. For example:


def outer():
    print("outer function")

    def inner():
        print("inner function")

    inner()


outer()
# outer function
# inner function

"""
In this example, we defined a function called outer.

Inside the outer function, we defined another function called inner. And we called the inner function from the inside of the outer function.

Often, we say that the inner function is nested in the outer function. In practice, you define nested functions when you don’t want these functions to be global.

Both outer and inner have access to the global and built-in scopes as well as their local scopes.

And the inner function also has access to its enclosing scope, which is the scope of the outer function.

From the inner() function perspective, its enclosing scope is neither local nor global. And Python calls this a nonlocal scope.
"""


# Let’s modify the outer and inner functions:


def outerX():
    message = "outer function"
    print(message)

    def innerX():
        print(message)

    innerX()


outerX()
# outer function
# outer function


"""
When we call the outer function, Python creates the inner function and executes it.

When the inner function executes, Python doesn’t find the message variable in the local scope. So Python looks for it in the enclosing scope, which is the scope of the outer function: pic-1

"""
