"""
Accessing values in a Dictionary

- To access a value by key from a dictionary, you can use the square bracket notation or the get() method.

      dict[key]

"""

# 1) Using square bracket notation
# The following shows how to get the values associated with the key first_name and last_name in the person dictionary:

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "favorite_colors": ["blue", "green"],
    "active": True,
}
print(person["first_name"])  # John
print(person["last_name"])  # Doe


# 2) Using the get() method
# If you attempt to access a key that doesn’t exist, you’ll get an error. For example:
# ssn = person["ssn"]  # err

# To avoid this error, you can use the get() method of the dictionary:
ssn = person.get("ssn")
print(ssn)  # None


""" 
  If the key doesn’t exist, the get() method returns None instead of throwing a KeyError. Note that None means no value exists.

  The get() method also returns a default value when the key doesn’t exist by passing the default value to its second argument.
"""


# The following example returns the '000-00-0000' string if the ssn key doesn’t exist in the person dictionary:

ssn = person.get("ssn", "000-00-0000")
print(ssn)  # 000-00-0000
