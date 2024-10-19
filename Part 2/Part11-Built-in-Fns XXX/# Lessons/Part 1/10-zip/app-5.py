"""
Unzip an iterable using the Python zip() function

- Unzipping reverses the zipping by converting the zipped values back to individual values.
- To unzip, you use the zip() function with the unpacking operator (*)

"""

names = ("John", "Jane", "Alice")
ages = (20, 22, 25)

employees = zip(names, ages)
# employees = (("John", 20), ("Jane", 22), ("Alice", 25))

names, ages = zip(*employees)

print(names)  # ('John', 'Jane', 'Alice')
print(ages)  # (20, 22, 25)

# In this example, we have a tuple where each element contains a name and age. The zip() function unpacks the tuple to create two different tuples (names and ages).


# Summary
# Use the zip() function to iterate iterables in parallel.
# Use the zip() function with the unpacking operator (*) to unzip values.
# Use itertool.zip_longest() function to zip iterables of different sizes.
