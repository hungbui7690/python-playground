"""
ZeroDivisionError

"""


# Now, if you don’t catch the ZeroDivisionError exception but the more general exception like Exception class:
# The program works as before because the try...except also catches the exception type that is the subclass of the Exception class.
def division(a, b):
    try:
        return {"success": True, "message": "OK", "result": a / b}
    except Exception as e:
        return {"success": False, "message": "b cannot be zero", "result": None}


# However, if you pass two strings instead of two numbers to the division() function, you’ll get the same message as if the ZeroDivisionError exception occurred:
result = division("10", "2")
print(result)
# {'success': False, 'message': 'b cannot be zero', 'result': None}


# In this example, the exception is not ZeroDivisionError but the TypeError. However, the code still handles it like the ZeroDivisionError exception.
