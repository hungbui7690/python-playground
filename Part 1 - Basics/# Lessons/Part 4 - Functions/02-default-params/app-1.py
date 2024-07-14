"""
Default Parameters
- When you call a function and pass an argument to the parameter that has a default value, the function will use that argument instead of the default value.

- However, if you don’t pass the argument, the function will use the default value.

- To use default parameters, you need to place parameters with the default values after other parameters. Otherwise, you’ll get a syntax error. For example, you cannot do something like this:

        def function_name(param1=value1, param2, param3):

"""


# The following example defines the greet() function that returns a greeting message:
def greet(name, message="Hi"):
    return f"{message} {name}"


# The greet() function has two parameters: name and message. And the message parameter has a default value of 'Hi'.
greeting = greet("John", "Hello")
print(greeting)  # Hello John
# Since we pass the second argument to the greet() function, the function uses the argument instead of the default value.


# The following example calls the greet() function without passing the second argument:
greeting = greet("John")
print(greeting)  # Hi John
