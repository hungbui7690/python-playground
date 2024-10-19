"""
TypeError

"""


# Therefore, you should always handle the exceptions from the most specific to the least specific. For example:
def division(a, b):
    try:
        return {"success": True, "message": "OK", "result": a / b}
    except TypeError as e:
        return {
            "success": False,
            "message": "Both a & b must be numbers",
            "result": None,
        }
    except ZeroDivisionError as e:
        return {"success": False, "message": "b cannot be zero", "result": None}
    except Exception as e:
        return {"success": False, "message": str(e), "result": None}


result = division("10", "2")
print(result)
# {'success': False, 'message': 'Both a & b must be numbers', 'result': None}


# In this example, we catch the TypeError, ZeroDivisionError, and Exception in the order that they appear in the try...except statement.
