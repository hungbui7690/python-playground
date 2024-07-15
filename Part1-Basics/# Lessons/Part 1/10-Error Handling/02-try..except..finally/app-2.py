"""
The try...except...finally

"""


# The try clause in the following example doesn’t cause an error. Therefore, all statements in the try and finally clauses execute:

a = 10
b = 2

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Finishing up.")
