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

# 2) Looping through all the keys in a dictionary
# Sometimes, you just want to loop through all keys in a dictionary. In this case, you can use a for loop with the keys() method.
# The keys() method returns an object that contains a list of keys in the dictionary.

for key in person.keys():
    print(key)

"""
  first_name
  last_name
  age
  favorite_colors
  active
"""


# In fact, looping through all keys is the default behavior when looping through a dictionary. Therefore, you don’t need to use the keys() method.
# The following code returns the same output as the one in the above example:

for key in person:
    print(key)
