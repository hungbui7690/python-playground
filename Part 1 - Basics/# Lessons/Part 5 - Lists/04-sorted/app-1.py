"""
sorted
- The sort() method sorts a list in place. In other words, it changes the order of elements in the original list.

- To return the new sorted list from the original list, you use the sorted() function:

      sorted(list)

- The sorted() function doesn’t modify the original list.

- By default, the sorted() function sorts the elements of the list from lowest to highest using the less-than operator (<).

- If you want to reverse the sort order, you pass the reverse argument as True like this:

      sorted(list,reverse=True)

"""


# 1) Using Python sorted() function to sort a list of strings
# The following example uses the sorted() function to sort a list of strings in alphabetical order:

guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
sorted_guests = sorted(guests)

print(guests)  # ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
print(sorted_guests)  # ['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']


# As you can see clearly in the output, the original list doesn’t change. The sorted() method returns a new sorted list from the original list.
# The following example uses the sorted() function to sort the guests list in the reverse alphabetical order:
guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
sorted_guests = sorted(guests, reverse=True)

print(sorted_guests)  # ['Robert', 'Patricia', 'Mary', 'John', 'Jennifer', 'James']
