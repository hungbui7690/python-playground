"""
Removing key-value pairs

- To remove a key-value pair by a key, you use the del statement:

      del dict[key]

- In this syntax, you specify the dictionary name and the key that you want to remove.

"""

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}


# The following example removes the key 'active' from the person dictionary:
del person["active"]
print(person)
# {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'favorite_colors': ['blue', 'green']}
