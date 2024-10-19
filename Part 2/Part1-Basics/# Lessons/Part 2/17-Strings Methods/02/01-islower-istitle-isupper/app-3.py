"""
ISTITLE
- Here is the syntax of the isupper() method:

    str.isupper()

- The string isupper() method returns True if all cased characters in a string are uppercase. Otherwise, it returns False.

- If the string doesn’t contain any cased characters, the isupper() method also returns False.

- In Python, cased characters are the ones with general category property being one of:

    Lu( letter, uppercase)
    Ll(letter, uppercase)
    Lt (letter, titlecase)

- Notice that to return a copy of the string with all cased characters converted to uppercase, you use the string upper() method.

"""


# The following example uses the isupper() to check if all cased characters of a string are uppercase:

message = "PYTHON"
is_uppercase = message.isupper()
print(is_uppercase)  # True


# However, the following example returns False because the string contains some characters in lowercase:

language = "Python"
is_uppercase = language.isupper()
print(is_uppercase)  # False


# The following example also returns False because the string doesn’t has any cased characters:

amount = "$100"
is_uppercase = amount.isupper()
print(is_uppercase)  # False
