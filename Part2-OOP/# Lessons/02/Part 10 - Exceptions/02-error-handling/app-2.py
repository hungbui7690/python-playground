"""
Exception Handling


"""


# A better approach is to raise an exception to the caller if the ZeroDivisionError exception occurred.
# In this example, the divide() function will raise an error if b is zero. To use the divide() function, you need to catch the ValueError exception:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("The second argument (b) must not be zero")


try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
else:
    print("result:", result)

# The second argument (b) must not be zero


# It’s a good practice to raise an exception instead of returning None in special cases.
