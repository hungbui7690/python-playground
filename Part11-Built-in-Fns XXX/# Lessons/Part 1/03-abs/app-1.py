"""
ABS
- returns an absolute value of a number

    abs(x)

- In this syntax, x can be an integer, a floating point number, or a complex number. If x is a complex number, the abs() returns the magnitude of that complex number.

- Also, x can be an object that implements the __abs__() method. In this case, the abs() function will delegate to the __abs__() method.

"""

# 1) Using abs() function with numbers
balance = -10
print(abs(balance))  # 👉 10

owed_amount = -20.99
print(abs(owed_amount))  # 👉 20.99

c = 3 - 5j
print(abs(c))  # 👉 5.0
