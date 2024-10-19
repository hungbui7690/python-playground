"""
ISLOWER
- The following shows the syntax of the string islower() method:

    str.islower()

- The string islower() method returns True if all cased characters are lowercase. Otherwise, it returns False.

- If the string doesn’t contain any cased characters, the islower() method also returns False.

- In Python, cased characters are the ones with general category property being one of:

    Lu (letter, uppercase)
    Ll (letter, lowercase)
    Lt (letter, titlecase)

- Note that to return a copy of the string with all characters converted to lowercase, you use the string lower() method.

"""


# The following example uses the islower() to check if all characters of an email are lowercase:

email = "hello@example.com"
is_lowercase = email.islower()
print(is_lowercase)  # True


# However, the following example returns False because the first character of the string is uppercase:

email = "Admin@example.com"
is_lowercase = email.islower()
print(is_lowercase)  # False


# The following example return False because the string has no cased characters:

number_str = "123"
is_lowercase = number_str.islower()
print(is_lowercase)  # False
