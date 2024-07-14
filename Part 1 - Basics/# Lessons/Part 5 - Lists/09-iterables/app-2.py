"""
What is an iterator

- An iterable can be iterated over. And an iterator is the agent that performs the iteration.

"""


# To get an iterator from an iterable, you use the iter() function. For example:

colors = ["red", "green", "blue"]
colors_iter = iter(colors)
print(colors_iter)  # <list_iterator object at 0x000001A4F2AFA4A0>


# Once you have the iterator, you can get the next element from the iterable using the next() function:

colors = ["red", "green", "blue"]
colors_iter = iter(colors)
color = next(colors_iter)
print(color)  # red


# Every time, you call the next() function, it returns the next element in the iterable. For example:

colors = ["red", "green", "blue"]
colors_iter = iter(colors)

color = next(colors_iter)
print(color)  # red

color = next(colors_iter)
print(color)  # green

color = next(colors_iter)
print(color)  # blue


# If there isn’t any more element and you call the next() function, you’ll get an exception.
# color = next(colors_iter)
# print(color)  # error
"""
  The iterator is stateful. It means that once you consume an element from the iterator, it’s gone.

  In other words, once you complete looping over an iterator, the iterator becomes empty. If you iterate over it again, it’ll return nothing.
"""


# Since you can iterate over an iterator, the iterator is also an iterable object. This is quite confusing. For example:

colors = ["red", "green", "blue"]
iterator = iter(colors)

for color in iterator:
    print(color)

# If you call the iter() function and pass an iterator to it, it’ll return the same iterator back.


"""
  Summary

      An iterable is an object that can be iterated over. An iterable has the ability to return one of its elements at a time.
      An iterator is an agent that performs iteration. It’s stateful. And an iterator is also an iterable object.
      Use the iter() function to get an iterator from an iterable object and the next() function to get the next element from the iterable object.

"""
