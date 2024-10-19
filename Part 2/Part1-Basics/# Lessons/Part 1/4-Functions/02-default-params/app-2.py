"""
Default Parameters


"""


# The following redefines the greet() function with the two parameters that have default values:
def greet(name="there", message="Hi"):
    return f"{message} {name}"


# In this example, you can call the greet() function without passing any parameters:
greeting = greet()
print(greeting)  # Hi there


# Suppose that you want the greet() function to return a greeting like Hello there. You may come up with the following function call:
# Unfortuntely, it returns an unexpected value:
greeting = greet("Hello")
print(greeting)  # Hi Hello


# Because when you pass the 'Hello' argument, the greet() function treats it as the first argument, not the second one.
# To resolve this, you need to call the greet() function using keyword arguments like this:
greeting = greet(message="Hello")
print(greeting)  # Hello there

"""
    Summary

        Use Python default parameters to simplify the function calls.
        Place default parameters after the non-default parameters.

"""
