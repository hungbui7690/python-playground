"""
ANY


"""

# 2) Using Python any() function to check if a string contains digits
# The following example checks if a string contains any digit:
message = "Python 101"

has_digit = False
for c in message:
    if c.isdigit():
        has_digit = True
        break

print(has_digit)  # True
# In this example, we iterate over characters of a string and check if each character is a digit. If so, set the has_digit flag to false and exit the loop.
# To make it shorter, you can use the any() method with a list comprehension.


# First, use a list comprehension to check if each character of a string is a digit and store the result in a list:
message = "Python 101"

digits = [c.isdigit() for c in message]
print(digits)  # [False, False, False, False, False, False, False, True, True, True]

has_digit = any(digits)
print(has_digit)  # False
