"""
Reduce a List into a Single Value
- Python offers a function called reduce() that allows you to reduce a list in a more concise way.

- Here is the syntax of the reduce() function:

      reduce(fn,list)

"""

# Reducing a list
# Sometimes, you want to reduce a list to a single value. For example, suppose that you have a list of numbers:

scores = [75, 65, 80, 95, 50]

# And to calculate the sum of all elements in the scores list, you can use a for loop like this:

total = 0

for score in scores:
    total += score

print(total)  # 365

# In this example, we have reduced the whole list into a single value, which is the sum of all elements from the list.
