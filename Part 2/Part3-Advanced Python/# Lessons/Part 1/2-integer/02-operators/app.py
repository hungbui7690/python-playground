"""
Python integer operations

- Python integers support all standard operations including:

    Addition +
    Subtraction –
    Multiplication *
    Division /
    Exponents **

"""

# The result of addition, subtraction, multiplication, and exponents of integers is an integer. For example:
a = 10
b = 20

c = a + b
print(c)  # 30
print(type(c))  # <class 'int'>


c = a - b
print(c)  # -1
print(type(c))  # <class 'int'>


c = a * b
print(c)  # 200
print(type(c))  # <class 'int'>

c = a**b
print(c)  # 100000000000000000000
print(type(c))  # <class 'int'>


# However, the division of two integers always returns a floating-point number. For example:
a = 10
b = 5
c = a / b
print(c)  # 2.0
print(type(c))  # <class 'float'>


# Summary
# Integers are whole numbers that include negative whole numbers, zero, and positive whole numbers.
# Computers use binary numbers to represent integers.
# Python uses a variable number of bits to represent integers. Therefore, the largest integer number that Python can represent depends on the available memory of the computer.
# In Python, all integers are instances of the class int.
# Use the getsizeof() function of the sys module to get the number of bytes of an integer.
# Python integers support all standard operations including addition, subtraction, multiplication, division, and exponent.
