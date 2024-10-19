"""
ISDECIMAL
- The string isdecimal() method returns True if the string:

    contains all characters that decimal characters.
    and has at least one character.

- Otherwise, it returns False.

- The following shows the syntax of isdecimal() method:

    str.isdecimal()

- Decimal characters are characters used to form numbers in base 10.

- The superscripts are digits, not decimal characters, therefore, the isdecimal() returns False if the string contains a superscript character.

- Likewise, Roman numerals, currency numerators, and fractions are numeric characters, not decimal characters. So the isdecimal() method also returns False if the string contains at least one of these characters.

"""

# The following example uses the isdecimal() method to check if all characters in a string are decimal characters:
quantity = "150"
print(quantity.isdecimal())  # True


# The following example returns False because the string contains the character '.' which is not a decimal character:
price = "99.9"
print(price.isdecimal())  # False
