"""
Partial Functions
- from the "functools" module.

"""


# The following example defines a function that multiplies two arguments:
def multiply(a, b):
    return a * b


# Sometimes, you just want to multiply an argument with a specified number e.g., 2. To do that, you can reuse the multiply function like this:
def double(a):
    return multiply(a, 2)


# The double function returns the multiply function. It passed the number 2 to the second argument of the multiply function.
# The following shows how to use the double function:
result = double(10)
print(result)  # 20


"""
    As you can see, the double function reduces the arguments of the multiply function.

    The double function freezes the second argument of the multiply function, which results in a new function with a simpler signature.

    In other words, double function reduces the complexity of the multiply function.

    In Python, the double function is called a partial function.

    In practice, you use partial functions when you want to reduce the number of arguments of a function to simplify the function’s signature.

    Since you’ll create partial functions sometimes, Python provides you with the partial function from the functools standard module to help you define partial functions more easily.

"""
