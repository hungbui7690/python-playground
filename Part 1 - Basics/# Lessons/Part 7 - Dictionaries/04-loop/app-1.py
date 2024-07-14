"""
Looping through a dictionary

- To examine a dictionary, you can use a for loop to iterate over its key-value pairs, or keys, or values.

** Note that since Python 3.7, when you loop through a dictionary, you’ll get the key-value pairs in the same order that you insert them.

"""

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}

# 1) Looping all key-value pairs in a dictionary
# Python dictionary provides a method called items() that returns an object which contains a list of key-value pairs as tuples in a list.

print(person.items())
# dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 25), ('favorite_colors', ['blue', 'green']), ('active', True)])


# To iterate over all key-value pairs in a dictionary, you use a for loop with two variable key and value to unpack each tuple of the list:

for key, value in person.items():
    print(f"{key}: {value}")

"""
  first_name: John
  last_name: Doe
  age: 25
  favorite_colors: ['blue', 'green']
  active: True
"""
# Note that you can use any variable name in the for loop. They don’t have to be the key and value.
