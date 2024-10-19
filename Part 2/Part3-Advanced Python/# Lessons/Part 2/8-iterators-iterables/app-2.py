"""
ITERATORS VS ITERABLES

Iterators

- An iterator is an object that implements the iterator protocol. In other words, an iterator is an object that implements the following methods:

    __iter__ returns the iterator object itself.
    __next__ returns the next element.

- Once you complete iterating a collection using an iterator, the iterator becomes exhausted. It means that you cannot use the iterator object anymore.

\\\\\\\\\\\\\\\\

Iterables

- An iterable is an object that you can iterate over.

!! An object is iterable when it implements the __iter__ method. And its __iter__ method returns a new iterator.

"""


# Examining the built-in list and list iterator
# !! In Python, a list is an ordered collection of items. It’s also an iterable because a list object has the __iter__ method that returns an iterator. For example:

numbers = [1, 2, 3]

number_iterator = numbers.__iter__()
print(type(number_iterator))  # <class 'list_iterator'>


# In this example, the __iter__ method returns an iterator with the type list_iterator.
# Because the list_iterator implements the __iter__ method, you can use the iter built-in function to get the iterator object:

numbers = [1, 2, 3]
number_iterator = iter(numbers)
print(type(number_iterator))  # <class 'list_iterator'>

# Since the list_iterator also implements the __next__ method, you can use the built-in function next to iterate over the list:

numbers = [1, 2, 3]
number_iterator = iter(numbers)

next(number_iterator)
next(number_iterator)
next(number_iterator)


# If you call the next function once more, you’ll get a StopIteration exception.
# next(number_iterator)  # StopIteration


# This is because the list iterator has been exhausted. To iterate the list again, you need to create a new iterator.
# This illustrates the separating the list from its iterator. The list is created once while the iterator is created every time you need to iterate over the list.
