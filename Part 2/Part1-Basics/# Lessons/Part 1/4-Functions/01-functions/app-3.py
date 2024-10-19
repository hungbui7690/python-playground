"""
Functions

"""


# Returning a value
# A function can perform a task like the greet() function. Or it can return a value. The value that a function returns is called a return value.
# To return a value from a function, you use the return statement inside the function body.


# The following example modifies the greet() function to return a greeting instead of displaying it on the screen:
def greet(name):
    return f"Hi {name}"


# When you call the greet() function, you can assign its return value to a variable:
greeting = greet("John")

# And show it on the screen:
print(greeting)

# The new greet() function is better than the old one because it doesn’t depend on the print() function.
# Later, you can reuse the greet() function in other applications. For example, you can use it in a web application to greet users after they log in.
