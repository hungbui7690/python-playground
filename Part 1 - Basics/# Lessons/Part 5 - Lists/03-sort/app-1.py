"""
Sort List
- To sort a list, you use the sort() method:

      list.sort()

- The sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list.

- By default, the sort() method sorts the elements of a list using the less-than operator (<). In other words, it places the lower elements before the higher ones.

- To sort elements from higher to lower, you pass the reverse=True argument to the sort() method like this:

      list.sort(reverse=True)

- To sort elements by a key

      list.sort(key=Key, reverse=True)

"""


# 1) Using the Python List sort() method to sort a list of strings
# If a list contains strings, the sort() method sorts the string elements alphabetically.
# The following example uses the sort() method to sort the elements in the guests list alphabetically:

guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
guests.sort()
print(guests)  # ['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']


# And the following example uses the sort() method with the reverse=True argument to sort the elements in the guests list in the reverse alphabetical order:

guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
guests.sort(reverse=True)
print(guests)  # ['Robert', 'Patricia', 'Mary', 'John', 'Jennifer', 'James']


# 2) Using the Python List sort() method to sort a list of numbers
# If a list contains numbers, the sort() method sorts the numbers from smallest to largest.
# The following example uses the sort() method to sort numbers in the scores list from smallest to largest:

scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)  # [4, 5, 6, 7, 8, 9]


# To sort numbers from the largest to smallest, you use the sort(reverse=True) like this:
scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)
print(scores)  # [9, 8, 7, 6, 5, 4]


# 3) Using the Python List sort() method to sort a list of tuples
# Suppose that you have a list of tuples like this:
companies = [("Google", 2019, 134.81), ("Apple", 2019, 260.2), ("Facebook", 2019, 70.7)]
# And you want to sort the companies list by revenue from highest to lowest. To do it:


# First, specify a sort key and pass it to the sort() method. To define a sort key, you create a function that accepts a tuple and returns the element that you want to sort by:
def sort_key(company):
    return company[2]


# This sort_key() function accepts a tuple called company and returns the third element.
# Note that the company is a tuple e.g., ('Google', 2019, 134.81). And the company[2] references the revenue like 134.81 in this case.

# Second, pass the sort_key function to the sort() method:
# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(
    companies
)  # [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]
