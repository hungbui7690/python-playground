"""
Transform List Elements with Python map() Function
- When working with a list (or a tuple), you often need to transform the elements of the list and return a new list that contains the transformed element.

- Convert iterator to a list

      list(iterator)

"""

# Suppose, you want to double every number in the following bonuses list:
bonuses = [100, 200, 300]

# To do it, you can use a for loop to iterate over the elements, double each of them, and add it to a new list like this:
new_bonuses = []

for bonus in bonuses:
    new_bonuses.append(bonus * 2)

print(new_bonuses)  # [200, 400, 600]

# Python provides a nicer way to do this kind of task by using the map() built-in function.
# The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.


# The following shows the basic syntax of the map() function:
#   iterator = map(fn, list)
# In this syntax, fn is the name of the function that will call on each element of the list.
# In fact, you can pass any iterable to the map() function, not just a list or tuple.


# Back to the previous example, to use the map() function, you define a function that doubles a bonus first and then use the map() function as follows:


def double(bonus):
    return bonus * 2


bonuses = [100, 200, 300]
iterator = map(double, bonuses)
print(iterator)  # <map object at 0x000001AA9D9BBA00>


# Or you make this code more concise by using a lambda expression like this:

bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus * 2, bonuses)


# Once you have an iterator, you can iterate over the new elements using a for loop.
# Or you can convert an iterator to a list by using the the list() function:

bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus * 2, bonuses)
print(list(iterator))  # [200, 400, 600]
