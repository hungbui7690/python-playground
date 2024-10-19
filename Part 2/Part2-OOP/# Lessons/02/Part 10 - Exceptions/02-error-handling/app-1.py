"""
Exception Handling
- To handle exceptions, you use the try statement. The try statement has the following clauses:

        try:
            # code that you want to protect from exceptions
        except <ExceptionType> as ex:
            # code that handle the exception
        finally:
            # code that always execute whether the exception occurred or not
        else:
            # code that executes if try execute normally (an except clause must be present)


- Let’s examine the try statement in greater detail.

\\\\\\\\\\\\\\\

try

- In the try clause, you place the code that protects from one or more potential exceptions. It’s a good practice to keep the code as short as possible. Often, you’ll have a single statement in the try clause.

- The try clause appears exactly one time in the try statement.

\\\\\\\\\\\\\\\

except

- In the except clause, you place the code that handles a specific exception type. A try statement can have zero or more except clauses. Typically, each except clause handles different exception types in specific ways.

- In an except clause, the as ex is optional. And the <ExceptionType> is also optional. However, if you omit the <ExceptionType> as ex, you’ll have a bare exception handler.

- When specifying exception types in the except clauses, you place the most specific to least specific exceptions from top to bottom.

- If you have the same logic that handles different exception types, you can group them in a single except clause. For example:

        try:
        ...
        except <ExceptionType1> as ex:
            log(ex)
        except <ExceptionType2> as ex:
            log(ex)

- Become

        try:
        ...
        except (<ExceptionType1>, <ExceptionType2>) as ex:
            log(ex)

- It’s important to note that the except order matters because Python will run the first except clause whose exception type matches the occurred exception.

\\\\\\\\\\\\\\\

finally

- The finally clause may appear zero or 1 time in a try statement. The finally clause always executes whether an exception occurred or not.

\\\\\\\\\\\\\\\

else

- The else clause also appears zero or 1 time. And the else clause is only valid if the try statement has at least one except clause.

- Typically, you place the code that executes if the try clause terminates normally.


"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        return None


result = divide(10, 0)

# if result is not None:
if result:
    print("result:", result)
else:
    print("Invalid inputs")


# Invalid inputs
