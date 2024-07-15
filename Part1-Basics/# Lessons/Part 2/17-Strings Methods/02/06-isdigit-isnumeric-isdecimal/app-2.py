"""
ISNUMERIC
- The string isnumeric() method returns True if:

    All characters in a string are numeric
    and the string contains at least one character.

- The following shows the syntax of the isnumeric() method:

    str.isnumeric()

- Like isdigit() method, the isnumeric() method returns True if all characters in the string are numeric characters 0-9.

- In addition, it also returns True if the string contains characters used in place of digits in other languages

"""

# For example, in Chinese, the number 1,2,3 is counted as 一，二，三. The isnumeric() returns True for these numeric characters:
result = "一二三".isnumeric()
print(result)  # True


# However, the isdigit() method returns False in this case:
result = "一二三".isdigit()
print(result)  # False
# This is the main difference between the isnumeric() and isdigit() methods.


# The following example uses the isnumeric() method to determine if all characters are numeric characters:
amount = "123"
result = amount.isnumeric()
print(result)  # True


# All the characters in the strings '99.99' and '-10' are not numeric, therefore, the isnumeric() method returns False:
price = "99.99"
print(price.isnumeric())  # False
discount = "-10"
print(discount.isnumeric())  # False
