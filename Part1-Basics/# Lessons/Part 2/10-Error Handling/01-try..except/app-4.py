"""
Handling multiple exceptions
- The try...except allows you to handle multiple exceptions by specifying multiple except clauses:

    try:
        # code that may cause an exception
    except Exception1 as e1:
        # handle exception
    except Exception2 as e2:
        # handle exception
    except Exception3 as e3:
        # handle exception

- This allows you to respond to each type of exception differently.
- If you want to have the same response to some types of exceptions, you can group them into one except clause:

    try:
        # code that may cause an exception
    except (Exception1, Exception2):
        # handle exception

"""


# The following example shows how to use the try...except to handle the ValueError and ZeroDivisionError exceptions:

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
except ZeroDivisionError:
    print("Error! The prior net sales cannot be zero.")


"""
    When you enter zero for the net sales of the prior period:

        Enter the net sales for
        - Prior period:0
        - Current period:120
        
    … you’ll get the following error:

        Error! The prior net sales cannot be zero.
"""
