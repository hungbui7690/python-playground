"""
Iterate over a List

      for item in list:
            # process the item

- The enumerate() function returns a tuple that contains the current index and element of the list.




"""


# For example, the following defines a list of cities and uses a for loop to iterate over the list:

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for city in cities:
    print(city)


# Iterate over a list with index
# Sometimes, you may want to access indexes of elements inside the loop. In these cases, you can use the enumerate() function.
# The enumerate() function returns a tuple that contains the current index and element of the list.
# The following example defines a list of cities and uses a for loop with the enumerate() function to iterate over the list:
cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for item in enumerate(cities):
    print(item)


# To access the index, you can unpack the tuple within the for loop statement like this:

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for index, city in enumerate(cities):
    print(f"{index}: {city}")


# The enumerate() function allows you to specify the starting index which defaults to zero.
# The following example uses the enumerate() function with the index that starts from one:

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for index, city in enumerate(cities, 1):
    print(f"{index}: {city}")
