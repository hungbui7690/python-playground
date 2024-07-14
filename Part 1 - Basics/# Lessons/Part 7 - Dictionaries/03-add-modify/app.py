"""
\\\\\\\\\\\\\\\\\\\\\\\\\\
Adding new key-value pairs

- Since a dictionary has a dynamic structure, you can add new key-value pairs to it at any time.

- To add a new key-value pair to a dictionary, you specify the name of the dictionary followed by the new key in square brackets along with the new value.


\\\\\\\\\\\\\\\\\\\\\\\\\\
Modifying values in a key-value pair

- To modify a value associated with a key, you specify the dictionary name with the key in square brackets and the new value associated with the key:

      dict[key] = new_value

"""

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}

# The following example adds a new key-value pair to the person dictionary:
person["gender"] = "male"


# The following example modifies the value associated with the age of the person dictionary:
person["age"] = 26

print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 26, 'favorite_colors': ['blue', 'green'], 'active': True}
