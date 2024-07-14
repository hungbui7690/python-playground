"""
Find the Index of an Element in a List
- To find the index of an element in a list, you use the index() function.

      cities.index(element)

- Check if an element in the list:
      if city in cities:

"""


# The following example defines a list of cities and uses the index() method to get the index of the element whose value is 'Mumbai':

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

result = cities.index("Mumbai")
print(result)  # 3


# However, if you attempt to find an element that doesn’t exist in the list using the index() function, you’ll get an error.
# This example uses the index() function to find the Osaka city in the cities list:

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

result = cities.index("Osaka")  # ValueError: 'Osaka' is not in list
print(result)


# To fix this issue, you need to use the in operator.
# The in operator returns True if a value is in the list. Otherwise, it returns False.
# Before using the index() function, you can use the in operator to check if the element that you want to find is in the list. For example:

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]
city = "Osaka"

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
