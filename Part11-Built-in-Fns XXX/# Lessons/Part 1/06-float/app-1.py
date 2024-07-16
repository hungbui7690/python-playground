"""
float
- convert a number or a string to a floating point number.
- The float() accepts a string or an number, either an integer or a floating-point number, and converts it to a floating-point number, if possible:

    float(x)

- If x is a string, it should contain a decimal number. Also, it can have an optional sign like a minus (-) or plus (+).
- If x is an integer or a floating point number, the float() returns the same floating point number with the same value. If the value is outside the range of a Python float, the float() will raise an OverflowError.
- If x is an object, the float() delegates to the x.__float__() method. If the object x does not have the __float__() method, the float() will use the __index__() method.


- The x parameter is optional. If you omit it, the float() will return 0.0.

"""


# 1) Using float() to convert a string to a floating point number
# The following example uses the float() to convert strings to floating point numbers:

f = float("+1.99")
print(f)  # 👉 1.99

f = float("-5.99")
print(f)  # 👉 -5.99

f = float("199e-001")
print(f)  # 👉 19.9

f = float("+1E3")
print(f)  # 👉 1000.0

f = float("-Infinity")
print(f)  # 👉 -inf


# 2) Using float() to convert an integer to a floating point number
# The following example uses the float() to convert integers to floating point numbers:

f = float(10)
print(f)  # 👉 10.0

f = float(-20)
print(f)  # 👉 -20.0

f = float(0)
print(f)  # 👉 0.0

f = float()
print(f)  # 👉 0.0
