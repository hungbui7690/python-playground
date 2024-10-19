"""
TypeError

"""


# If the code that handles different exceptions are the same, you can group all exceptions into one as follows:


def division(a, b):
    try:
        return {"success": True, "message": "OK", "result": a / b}
    except (TypeError, ZeroDivisionError, Exception) as e:
        return {"success": False, "message": str(e), "result": None}


result = division(10, 0)
print(result)
# {'success': False, 'message': 'division by zero', 'result': None}


# Summary
# Python exceptions are objects of classes, which are the subclasses of the BaseException class.
# Do handle the exception from the most specific to lest specific.
