"""
ISALNUM
- The string isalnum() method returns True if:

    all characters in the string are alphanumeric
    and the string has at least one character.

- Otherwise, it returns False.

- The following shows the syntax of the isalnum() method:

    str.isalnum()

- Functionally, the string str contains only alphanumeric characters if one of the following methods returns True:

    str.isalpha()
    str.isnumeric()
    str.isdecimal()
    str.isalpha()

"""

# The following example uses the isalnum() method to check if the string 'Python3' contains only alphanumeric characters:
version = "Python3"
result = version.isalnum()
print(result)  # True
# It returns True because the string 'Python3' contains only letters and numbers.


# The following example returns False because the string 'Python 3' contains a whitespace:
version = "Python 3"
result = version.isalnum()
print(result)  # False
