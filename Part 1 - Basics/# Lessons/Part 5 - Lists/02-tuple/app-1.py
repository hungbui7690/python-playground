"""
Tuples
- Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.

- A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.

"""


# Defining a tuple

# A tuple is like a list except that it uses parentheses () instead of square brackets [].
# The following example defines a tuple called rgb:

rgb = ("red", "green", "blue")


# Once defining a tuple, you can access an individual element by its index. For example:

rgb = ("red", "green", "blue")

print(rgb[0])  # red
print(rgb[1])  # green
print(rgb[2])  # blue


# Since a tuple is immutable, you cannot change its elements. The following example attempts to change the first element of the rgb tuple to 'yellow':

rgb = ("red", "green", "blue")
rgb[0] = "yellow"  # TypeError: 'tuple' object does not support item assignment


# Defining a tuple that has one element
# To define a tuple with one element, you need to include a trailing comma after the first element. For example:

numbers = (3,)
print(type(numbers))  # <class 'tuple'>


# If you exclude the trailing comma, the type of the numbers will be int , which stands for integer. And its value is 3. Python won’t create a tuple that includes the number 3:

numbers = 3  # prettier will remove the () if we don't add ,
print(type(numbers))  # <class 'int'>
