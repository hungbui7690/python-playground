"""
\\\\\\\\\\\\\\\\\\\\
Dictionary
- allows you to organize related information.


\\\\\\\\\\\\\\\\\\\\
Introduction to the Python Dictionary type

- A Python dictionary is a collection of key-value pairs where each key is associated with a value.

- A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. In fact, you can use a value of any valid type in Python as the value in the key-value pair.

- A key in the key-value pair must be immutable. In other words, the key cannot be changed, for example, a number, a string, a tuple, etc.

- Python uses curly braces {} to define a dictionary. Inside the curly braces, you can place zero, one, or many key-value pairs.
"""

# The following example defines an empty dictionary:

empty_dict = {}


# Typically, you define an empty dictionary before a loop, either for loop or while loop. And inside the loop, you add key-value pairs to the dictionary.
# To find the type of a dictionary, you use the type() function as follows:

print(type(empty_dict))  # <class 'dict'>


# The following example defines a dictionary with some key-value pairs:

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}

# The person dictionary has five key-value pairs that represent the first name, last name, age, favorite colors, and active status.
