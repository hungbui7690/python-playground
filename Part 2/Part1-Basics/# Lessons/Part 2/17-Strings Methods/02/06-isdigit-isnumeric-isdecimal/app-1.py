"""
ISDIGIT
- The string isdigit() method returns True if:

    1. All characters in the string are digits and
    2. The string has at least one character.

- Otherwise, it returns False.

- The following shows the syntax if the string isdigit() method:

    str.isdigit()

- The isdigit() method returns True if the string contains solely the digits (0-9). If a string contains a decimal point, minus, or plus sign, the isdigit() returns False.

*** Note that the isdigit() also returns True for a string that contains superscript like ’10²’.

"""

# The following example uses the isdigit() method to check if the all characters in a string are digits:
quantity = "100"
print(quantity.isdigit())  # True


# The following example returns False:
price = "9.99"
print(price.isdigit())  # False


# The following examples returns True because the Unicode character for 0 and 2 are digits:
x = "\u0030"  # unicode for 0
y = "\u00b2"  # unicode for ²

print(x.isdigit())  # True
print(y.isdigit())  # True


# The following example returns False because the string is empty:
empty = ""
print(empty.isdigit())  # False
