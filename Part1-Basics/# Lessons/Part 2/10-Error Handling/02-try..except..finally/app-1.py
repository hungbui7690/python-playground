"""
The try...except statement allows you to catch one or more exceptions in the try clause and handle each of them in the except clauses.

- The try...except statement also has an optional clause called finally:

    try:
        # code that may cause exceptions
    except:
        # code that handle exceptions
    finally:
        # code that clean up

- The finally clause always executes whether an exception occurs or not. And it executes after the try clause and any except clause.

"""


# The following example uses the try...catch...finally statement:

a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Finishing up.")

# In this example, the try clause causes a ZeroDivisionError exception both except and finally clause executes.
