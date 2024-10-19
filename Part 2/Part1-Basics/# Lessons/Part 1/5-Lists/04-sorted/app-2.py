"""
sorted

"""


# 2) Using Python sorted() function to sort a list of numbers
# The following example uses the sorted() function to sort a list of numbers from smallest to largest:

scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores)

print(sorted_scores)  # [4, 5, 6, 7, 8, 9]


# The following example uses the sorted() function with the reverse argument sets to True. It sorts a list of numbers from largest to smallest:

scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores, reverse=True)

print(sorted_scores)  # [9, 8, 7, 6, 5, 4]
