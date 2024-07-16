"""
ALL

"""

# 2) Using Python all() function to validate iterables of numbers
# The following example uses the all() function to check if all numbers of an iterable are greater than or equal to four:

ratings = [3, 5, 4, 2, 4, 5]
has_good_rating = all([rating >= 4 for rating in ratings])
print(has_good_rating)  # false


"""
How it works.

- First, use a list comprehension to convert the list of ratings to a list of True and False. The following

    [rating >= 4 for rating in ratings]

- returns a list of boolean values:

    [False, True, True, False, True, True]

- Second, pass the result of the list comprehension to all() function. So all() function returns False because the list contains some False elements.

"""
