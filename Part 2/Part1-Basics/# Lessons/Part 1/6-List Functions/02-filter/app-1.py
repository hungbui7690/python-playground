"""
Filter List Elements
- Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.

- The following shows the syntax of the filter() function:

      filter(fn, list)


"""

# Suppose that you have the following list of scores:

scores = [70, 60, 80, 90, 50]

# To get all elements from the scores list where each element is greater than or equal to 70, you use the following code:

filtered = []

for score in scores:
    if score >= 70:
        filtered.append(score)

print(filtered)  # [70, 80, 90]


"""
  How it works.

      First, define an empty list (filtered) that will hold the elements from the scores list.
      Second, iterate over the elements of the scores list. If the element is greater than or equal to 70, add it to the filtered list.
      Third, show the filtered list to the screen.

  Python has a built-in function called filter() that allows you to filter a list (or a tuple) in a more beautiful way.

  The following shows the syntax of the filter() function:

      filter(fn, list)

  The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements where the fn() returns True.

  In fact, you can pass any iterable to the second argument of the filter() function, not just a list.
"""

# The following shows how to use the filter() function to return a list of scores where each score is greater than or equal to 70:

scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)

print(list(filtered))  # [70, 80, 90]

# Since the filter() function returns an iterator, you can use a for loop to iterate over it. Or you can use the list() function to convert the iterator to a list.
