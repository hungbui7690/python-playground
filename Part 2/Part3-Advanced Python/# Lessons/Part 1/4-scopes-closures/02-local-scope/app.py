"""
Local Scopes

"""


# When creating a function, you can define parameters and variables for the function. For example:


def increment(counter, by=1):
    result = counter + by
    return result


"""
When you execute the code, Python carries two phases: compilation and execution.

When Python compiles the file, it adds the increment function to the global scope. In addition, Python determines that the counter, by, and result variables inside the increment() function will be local to the increment() function. And Python won’t create the counter, by and result variables until the function is executed.

Every time you call a function, Python creates a new scope. Python also assigns the variables defined inside the function to that scope. And this scope is called a function local scope or local scope.

In our example, when you call the increment() function:
"""
increment(10, 2)

"""
… Python creates a local scope for the increment() function call.

Also, Python creates local variables counter, by, and result in the local namespace and binds them to values 10, 2, and 12.

When the function completes, Python will delete the local scope. And all the local variables such as counter, by, and result variables are out of scope. If you attempt to access these variables from outside the increment() function, you’ll get an error.

And if you call the increment() function again:
"""
increment(100, 3)

""" 
… Python creates a new local scope and variables including counter, by and result, and binds them to values 100, 3, and 103.
"""
