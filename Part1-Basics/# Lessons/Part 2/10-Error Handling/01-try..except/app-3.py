"""
Catching specific exceptions

- When you enter the net sales of the prior period as zero, you’ll get the following message:

    Enter the net sales for
    - Prior period:0
    - Current period:100
    Error! Please enter a number for net sales.

- In this case, both net sales of the prior and current periods are numbers, but the program still issues an error message. Another exception must occur.

- The try...except statement allows you to handle a particular exception. To catch a selected exception, you place the type of exception after the except keyword:

    try:
        # code that may cause an exception
    except ValueError as error:
        # code to handle the exception

"""

try:
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
except ValueError:
    print("Error! Please enter a number for net sales.")


"""
    When you run a program and enter a string for the net sales, you’ll get the same error message.

    However, if you enter zero for the net sales of the prior period:

        Enter the net sales for
        - Prior period:0
        - Current period:100
        
    … you’ll get the following error message:

        Traceback (most recent call last):
        File "d:/python/try-except.py", line 9, in <module>
            change = (current - previous) * 100 / previous
        ZeroDivisionError: float division by zero


    This time you got the ZeroDivisionError exception. This division by zero exception is caused by the following statement:

        change = (current - previous) * 100 / previous
"""
