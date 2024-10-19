"""
ALL

"""

# 1) Using Python all() function to make a complex condition more simple
# The following example checks if the length of v is greater than zero and less than 25 and if it contains only alphanumeric characters:
v = "Python"
if len(v) > 0 and len(v) < 25 and v.isalnum():
    print(v)
# Python


# The condition is quite complex. To make it shorter, you can replace all the and operators with the all() function like this:
v = "Python"
valid = all([len(v) > 0, len(v) < 25, v.isalnum()])
if valid:
    print(v)
# Python
