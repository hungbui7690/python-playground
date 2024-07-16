"""
Bare exception handlers

- When you want to catch any exception, you can use the bare exception handlers. A bare exception handler does not specify an exception type:

    try:
        ...
    except:
        ...

- It’s equivalent to the following:

    try:
        ...
    except BaseException:
        ...

- A bare exception handler will catch any exceptions including the SystemExit and KeyboardInterupt exceptions.
- A bare exception will make it harder to interrupt a program with Control-C and disguise other programs.
- If you want to catch all exceptions that signal program errors, you can use except Exception instead:

    try:
        ...
    except Exception:
        ...

- In practice, you should avoid using bare exception handlers. If you don’t know exceptions to catch, just let the exception occurs and then modify the code to handle these exceptions.
- To get exception information from a bare exception handler, you use the exc_info() function from the sys module.

- The sys.exc_info() function returns a tuple that consists of three values:

    + type is the type of the exception occurred. It’s a subclass of the BaseException.
    _ value is the instance of the exception type.
    + traceback is an object that encapsulates the call stack at the point where the exception originally ocurred.

"""

# The following example uses the sys.exc_info() function to examine the exception when a string is divided by a number:

import sys

try:
    "20" / 2
except:
    exc_info = sys.exc_info()
    print(exc_info)
# (<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'str' and 'int'"), <traceback object at 0x000001E8C165EBC0>)


# The output shows that the code in the try clause causes a TypeError exception. Therefore, you can modify the code to handle it specifically as follows:
try:
    "20" / 2
except TypeError as e:
    print(e)
# unsupported operand type(s) for /: 'str' and 'int'


"""
Summary

    - Use the try statement to handle exception.
    - Place only minimal code that you want to protect from potential exceptions in the try clause.
    - Handle exceptions from most specific to least specific in terms of exception types. The order of except clauses is important.
    - The finally always executes whether the exceptions occurred or not.
    - The else clause only executes when the try clause terminates normally. The else clause is valid only if the try statement has at least one except clause.
    - Avoid using bare exception handlers.

"""
