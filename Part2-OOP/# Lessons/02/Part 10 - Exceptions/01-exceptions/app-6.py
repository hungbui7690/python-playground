"""
ZeroDivisionError

"""


# In this example, if b is zero, the ZeroDivisionError exception will occur. To handle the ZeroDivisionError exception, you use the try...except statement as follows:
def division(a, b):
    try:
        return {"success": True, "message": "OK", "result": a / b}
    except ZeroDivisionError as e:
        return {"success": False, "message": "b cannot be zero", "result": None}


result = division(10, 0)
print(result)
# {'success': False, 'message': 'b cannot be zero', 'result': None}

"""
In this example, the function returns a dictionary that has three elements:
    + success is a boolean value that indicates whether the operation is successful or not.
    + message indicates the error or success message.
    + result stores the result of a / b or None if b is zero.
"""
