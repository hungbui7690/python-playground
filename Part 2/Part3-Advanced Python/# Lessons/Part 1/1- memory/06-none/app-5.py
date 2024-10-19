"""
The applications of the Python None object

"""

# 3) Using the Python None object as a return value of a function
# When a function doesn’t have a return value, it returns None by default. For example:


def say(something):
    print(something)


result = say("Hello")
print(result)
# The say() function doesn’t return anything; therefore, it returns None.


# Summary
# None is a singleton object of the NoneType class.
# None is not equal to anything except itself.
# Use is or is not operator to compare None with other values.
