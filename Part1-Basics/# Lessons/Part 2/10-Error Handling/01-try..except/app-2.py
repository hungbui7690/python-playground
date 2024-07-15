"""
Handling exceptions


"""


# So to handle exceptions using the try...except statement, you place the code that may cause an exception in the try clause and the code that handles exceptions in the except clause.
# Here’s how you can rewrite the program and uses the try...except statement to handle the exception:

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
except:
    print("Error! Please enter a number for net sales.")


"""
    If you run the program again and enter the net sales which is not a number, the program will issue the message that you specified in the except block instead:

        Enter the net sales for
        - Prior period:100
        - Current period:120'
        Error! Please enter a number for net sales.
"""
