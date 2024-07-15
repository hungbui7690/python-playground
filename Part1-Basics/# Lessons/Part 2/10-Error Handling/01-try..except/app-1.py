"""
try..except
- In Python, there’re two main kinds of errors: syntax errors and exceptions.

"""

# Syntax errors
# When you write an invalid Python code, you’ll get a syntax error. For example:
# In this example, the Python interpreter detected the error at the if statement since a colon (:) is missing after it.

# current = 1
# if current < 10
# current += 1


# Exceptions
# Even though when your code has valid syntax, it may cause an error during execution.
# In Python, errors that occur during the execution are called exceptions. The causes of exceptions mainly come from the environment where the code executes. For example:
#     Reading a file that doesn’t exist.
#     Connecting to a remote server that is offline.
#     Bad user inputs.
# When an exception occurs, the program doesn’t handle it automatically. This results in an error message.
# For example, the following program calculates the sales growth:

# get input net sales
print("Enter the net sales for")

previous = float(input("- Prior period:"))
current = float(input("- Current period:"))

# calculate the change in percentage
change = (current - previous) * 100 / previous

# show the result
if change > 0:
    result = f"Sales increase {abs(change)}%"
else:
    result = f"Sales decrease {abs(change)}%"

print(result)


"""
    How it works.

        First, prompt users for entering two numbers: the net sales of the prior and current periods.
        Then, calculate the sales growth in percentage and show the result.



    When you run the program and enter 120' as the net sales of the current period, the Python interpreter will issue the following output:

        Enter the net sales for
        - Prior period:100
        - Current period:120'
        Traceback (most recent call last):
        File "d:/python/try-except.py", line 5, in <module>
            current = float(input('- Current period:'))
        ValueError: could not convert string to float: "120'"


    The Python interpreter showed a traceback that includes detailed information of the exception:

        The path to the source code file (d:/python/try-except.py) that caused the exception.
        The exact line of code that caused the exception (line 5)
        The statement that caused the exception current = float(input('- Current period:'))
        The type of exception ValueError
        The error message: ValueError: could not convert string to float: "120'"

    Because float() couldn’t convert the string 120' to a number, the Python interpreter issued a ValueError exception.

    In Python, exceptions have different types such as TypeError, NameError, etc.

"""
