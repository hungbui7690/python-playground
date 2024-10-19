"""
Sort List

"""

companies = [("Google", 2019, 134.81), ("Apple", 2019, 260.2), ("Facebook", 2019, 70.7)]


# Using lambda expression
# To make it more concise, Python allows you to define a function without a name with the following syntax:
# lambda arguments: expression


# A function without a name is called an anonymous function. And this syntax is called a lambda expression.
# Technically, it’s equivalent to the following function:
# def name(arguments):
#     return expression


# sort the companies by revenue
companies.sort(key=lambda company: company[2])

# show the sorted companies
print(companies)
# [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]


"""
  Summary

      Use the Python List sort() method to sort a list in place.
      The sort() method sorts the string elements in alphabetical order and sorts the numeric elements from smallest to largest.
      Use the sort(reverse=True) to reverse the default sort order.

"""
