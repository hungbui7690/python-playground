"""
Looping through a dictionary

"""

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}


# 3) Looping through all the values in a dictionary
# The values() method returns a list of values without any keys.
# To loop through all the values in a dictionary, you use a for loop with the values() method:

for value in person.values():
    print(value)

"""
  John
  Doe
  25
  ['blue', 'green']
  True
"""

"""
  Summary

      A Python dictionary is a collection of key-value pairs, where each key has an associated value.
      Use square brackets or get() method to access a value by its key.
      Use the del statement to remove a key-value pair by the key from the dictionary.
      Use for loop to iterate over keys, values, and key-value pairs in a dictionary.
"""
